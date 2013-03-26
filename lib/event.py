# For determining hostname
import socket

import logging
log = logging.getLogger(__name__)

class Events():
	def __init__(self):
		self.events = []

	def add(self, service, state, description, ttl, tags=None, metric=None, hostname=socket.gethostname()):
		event = {}
		event['service'] = service
		event['state'] = state
		event['description'] = description
		event['ttl'] = ttl
		event['hostname'] = hostname
		
		if tags is not None:
			event['tags'] = tags

		if metric is not None:
			event['metric'] = metric

		log.debug("Event added: %s" % (event))
		self.events.append(event)

	def send(self, client):
		log.debug("Sending %s events..." % (len(self.events)))
		while len(self.events) > 0:
			event = self.events.pop(0)
			client.send(event)

	