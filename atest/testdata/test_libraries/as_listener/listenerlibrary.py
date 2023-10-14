import sys


class listenerlibrary:
    ROBOT_LISTENER_API_VERSION = 2
    ROBOT_LIBRARY_SCOPE = "TEST CASE"

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        self.events = []
        self.level = 'suite'

    def get_events(self):
        return self.events[:]

    def _start_suite(self, name, attrs):
        self.events.append(f'Start suite: {name}')

    def endSuite(self, name, attrs):
        self.events.append(f'End suite: {name}')

    def _start_test(self, name, attrs):
        self.events.append(f'Start test: {name}')
        self.level = 'test'

    def end_test(self, name, attrs):
        self.events.append(f'End test: {name}')

    def _startKeyword(self, name, attrs):
        self.events.append(f'Start kw: {name}')

    def _end_keyword(self, name, attrs):
        self.events.append(f'End kw: {name}')

    def _close(self):
        level = f' ({self.level})' if self.ROBOT_LIBRARY_SCOPE == 'TEST CASE' else ''
        sys.__stderr__.write("CLOSING %s%s\n" % (self.ROBOT_LIBRARY_SCOPE, level))

    def events_should_be(self, *expected):
        self._assert(self.events == list(expected),
                     'Expected events:\n%s\n\nActual events:\n%s'
                     % (self._format(expected), self._format(self.events)))

    def events_should_be_empty(self):
        self._assert(not self.events,
                     'Expected no events, got:\n%s' % self._format(self.events))

    def _assert(self, condition, message):
        assert condition, message

    def _format(self, events):
        return '\n'.join(events)
