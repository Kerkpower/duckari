import typing as t

import hikari

__all__ = ["Duck"]


class Duck:
    def __init__(
        self, prefix: t.Optional[str], intents: hikari.Intents = hikari.Intents.ALL_UNPRIVILEGED, **kwargs: t.Any
    ) -> None:
        self._prefix: t.Optional[str] = prefix
        self._intents: hikari.Intents = intents
        self._hikari_bot: t.Optional[hikari.GatewayBot] = None
        self._extra_kwargs: t.Dict[str, t.Any] = kwargs

    async def on_message_create(self, event: hikari.MessageCreateEvent) -> None:
        assert self._prefix is not None

        if event.message.author.is_bot:
            return

        # Do command processing here :beanos:

    def run(self, token: str, **kwargs: t.Any) -> None:
        self._hikari_bot = hikari.GatewayBot(token, intents=self._intents, **self._extra_kwargs)

        if self._prefix is not None:
            self._hikari_bot.subscribe(hikari.MessageCreateEvent, self.on_message_create)

        self._hikari_bot.run(**kwargs)
