from LinkedList import LinkedList

def isIntersect(lla, llb):
	if lla.last != llb.last:
		return False
	shorter = lla if len(lla) < len(llb) else llb
	longer = lla if len(lla) > len(llb) else llb

	diff = len(longer) - len(shorter)
	for i in range(diff):
		longer = longer.next

		while shorter is not longer:
			shorter = shorter.next
			longer = longer.next

		return longer
