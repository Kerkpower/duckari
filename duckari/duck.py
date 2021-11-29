import collections
import typing as t

import hikari

__all__ = ["Duck"]

_ListenerT = t.Callable[[hikari.Event], t.Coroutine[t.Any, t.Any, None]]


class Command:
    def __init__(self, callback, name, aliases):
        self.callback = callback
        self.name = name
        self.aliases = []
        self.conditions = []

    def add_alias(self, alias):
        self.aliases.append(alias)

    def add_condition(self, condition):
        self.conditions.append(condition)


class Duck:
    def __init__(
        self,
        prefix: t.Optional[str],
        intents: hikari.Intents = hikari.Intents.ALL_UNPRIVILEGED,
        **kwargs: t.Any
    ) -> None:
        self._prefix: t.Optional[str] = prefix
        self._intents: hikari.Intents = intents
        self._hikari_bot: t.Optional[hikari.GatewayBot] = None
        self._extra_kwargs: t.Dict[str, t.Any] = kwargs
        self._listeners: t.Dict[
            t.Type[hikari.Event], t.List[_ListenerT]
        ] = collections.defaultdict(list)
        self._commands: dict = {}  # TODO: Add better type

    def listen(
        self, event: t.Type[hikari.Event]
    ) -> t.Callable[[_ListenerT], _ListenerT]:
        def decorate(func: _ListenerT) -> _ListenerT:
            self._listeners[event].append(func)
            return func

        return decorate

    def command(self, name: str = None):  # TODO: Add return type
        def decorate(func: _ListenerT) -> _ListenerT:
            self._commands[name].append(
                func
            )  # You can add multiple callbacks for a command.
            return func

        return decorate

    async def on_message_create(self, event: hikari.MessageCreateEvent) -> None:
        assert self._prefix is not None

        if event.message.author.is_bot:
            return

        if event.message.content.startswith(self._prefix):
            content_without_prefix = event.message.content.replace(self._prefix, "", 1)
            if content_without_prefix.split()[0] in self._commands.keys():
                for callback in self._commands[content_without_prefix.split()[0]]:
                    callback()  # TODO: Add context
            # TODO: Add command not found error

    def run(self, token: str, **kwargs: t.Any) -> None:
        self._hikari_bot = hikari.GatewayBot(
            token, intents=self._intents, **self._extra_kwargs
        )

        if self._prefix is not None:
            self._hikari_bot.subscribe(
                hikari.MessageCreateEvent, self.on_message_create
            )

        for event, listeners in self._listeners.items():
            for listener in listeners:
                self._hikari_bot.subscribe(event, listener)

        self._hikari_bot.run(**kwargs)
