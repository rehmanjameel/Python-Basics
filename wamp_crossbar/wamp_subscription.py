from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner


# or: from autobahn.asyncio.wamp import ApplicationSession

def light_on():
    print("Light on")


def light_off():
    print("Light off")


class MyComponent(ApplicationSession):

    async def onJoin(self, details):
        # 1. subscribe to a topic so we receive events
        def on_event(msg):
            print("Got event: {}".format(msg))
            if msg == "On":
                light_on()
            elif msg == "Off":
                light_off()

        await self.subscribe(on_event, 'org.codebase')
        print("subscribed")


if __name__ == '__main__':
    runner = ApplicationRunner("ws://0.0.0.0:8080/ws", realm="realm1")
    runner.run(MyComponent)
