import sys
from turtle import down

in_file_arg, out_file_arg, width_arg = sys.argv[1], sys.argv[2], sys.argv[3]

width = int(width_arg)
orig_text = ''

with open(in_file_arg, 'r', encoding='utf-8') as in_file:
    for line in in_file:
        orig_text += line

spaced_text = ''
last_newline_pos = -1
new_line = ''


i = -1
while i+1 < len(orig_text):
	i += 1
	next_newline_pos = None
	broke_at_newline = False

	if orig_text[i] == '\n':
		spaced_text += orig_text[last_newline_pos+1:i+1]
		last_newline_pos = i

	elif i - last_newline_pos == width:
		upstream = downstream = i

		while True:
			if upstream > last_newline_pos and orig_text[upstream] in [' ', '\n']:
				next_newline_pos = upstream

				if orig_text[upstream] == '\n':
					broke_at_newline = True

				break
			
			if orig_text[downstream] in [' ', '\n']:
				next_newline_pos = downstream

				if orig_text[downstream] == '\n':
					broke_at_newline = True

				break

			downstream += 1
			upstream -= 1

		# Don't include the previous newline; include the current space before the next newline
		spaced_text += orig_text[last_newline_pos+1:next_newline_pos+1]
		if not broke_at_newline:
			spaced_text += '\n'
		last_newline_pos = next_newline_pos

		i = next_newline_pos


with open(out_file_arg, 'w', encoding='utf-16') as out_file:
    out_file.write(spaced_text)
