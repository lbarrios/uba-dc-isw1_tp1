
class ContextGraph: 

	def __init__(self, name="grafo"):
		self.name = name
		self.agents = []
		self.contexts = []
		self.events = []

	def add_event(self, orig, dest, event, context):
		if not orig in self.agents: self.agents.append( orig )
		if not dest in self.agents: self.agents.append( dest )
		if not context in self.contexts: self.contexts.append( context )

		self.events.append({
			'orig' : orig,
			'dest' : dest,
			'event': event, 
			'context' : context
		})

	def context_color(self, context):
		colors = ["aquamarine", "bisque", "cyan", "deepskyblue1", "chocolate", "red", "blue", "cadetblue", "gold", "gray", "green", "indigo", "lightcoral", "orangered", "red3"]

		return colors[ self.contexts.index(context) ]

	def print_as_dot(self, edges_labeled=True):
		print "digraph %s {" % (self.name, )
		print '\trankdir=LR;'
		print '\tnode [shape=box, style=rounded, fontsize=24]'

		for agent in self.agents:
			if agent == "Sistema":
				print '\t"%s" [shape=record, label="{|%s|}"]' % (agent, agent)
			else:
				print '\t"%s";' % (agent,)

		for event in self.events:
			if edges_labeled:
				print '\t"%s" -> "%s" [color="%s" label="%s"];' % (event["orig"], event["dest"], self.context_color(event["context"]), event["event"])
			else:
				print '\t"%s" -> "%s" [color="%s"];' % (event["orig"], event["dest"], self.context_color(event["context"]))

		print "}"