import math

hex_to_bin = {'0':'0000',
			'1':'0001',
			'2':'0010',
			'3':'0011',
			'4':'0100',
			'5':'0101',
			'6':'0110',
			'7':'0111',
			'8':'1000',
			'9':'1001',
			'A':'1010',
			'B':'1011',
			'C':'1100',
			'D':'1101',
			'E':'1110',
			'F':'1111'}

binary = ""
with open('input16.txt', 'r') as f:
	for char in f.readline():
		binary += hex_to_bin[char]

def func_0 (l): 
	return sum(l)

def func_1 (l): 
	return math.prod(l)

def func_2 (l): 
	return min(l)

def func_3 (l): 
	return max(l)

def func_5 (l): 
	return 1 if l[0] > l[1] else  0

def func_6 (l): 
	return 1 if l[0] < l[1] else 0

def func_7 (l): 
	return 1 if l[0] == l[1] else 0

functions = dict(zip([0, 1, 2, 3, 5, 6, 7], [func_0, func_1, func_2, func_3, func_5, func_6, func_7]))

def parse(packet):
	version = int(packet[0:3], 2)
	type_id = int(packet[3:6], 2)
	if (type_id == 4): 
		literal = ""
		for i in range(6, len(packet), 5):
			leading_bit = packet[i]
			literal += packet[i+1:i+5]
			if (leading_bit == '0'): 
				break
		return {'value': int(literal, 2), 'position': i+5, 'version': version}
	else: 
		length_id = packet[6]
		values = []
		if (length_id == '0'):
			total_length = int(packet[7:22], 2)		
			current_pos = 22
			end_pos = current_pos + total_length
			while (current_pos < end_pos):
				p = parse(packet[current_pos:end_pos]) 
				current_pos += p['position']
				values.append(p['value'])
				version += p['version']
		else:
			num_packets = int(packet[7:18], 2)
			current_pos = 18
			count = 0
			while (count < num_packets):
				p = parse(packet[current_pos:])
				current_pos += p['position']
				values.append(p['value'])
				version += p['version']
				count += 1
		return {'value': functions[type_id](values), 'position': current_pos, 'version': version}

ans = parse(binary)
print(ans['version'])
print(ans['value'])