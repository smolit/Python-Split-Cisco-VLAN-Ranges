import string

text =(input("Please paste Cisco VLAN-Range here: "))

text = text.replace(" ", "")

vlan_array = text.split(',')

print ("\nOutput:\n")

for y in range (0,len(vlan_array)):

	if (vlan_array[y].find('-')) != -1:
		vlan_range = vlan_array[y]
		vlan_range_array = []

		vlan_range_array = vlan_range.split('-')

		start = int(vlan_range_array[0])
		ende = int(vlan_range_array[1])

		for x in range (start,ende+1):
			print (x)
	else:
		print (vlan_array[y])
	#neuer Kommentar
	# second new comment