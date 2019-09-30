# -*- coding: utf-8 -*-

import re

def find_str(ori_str, sub_str):

	pos_list = []
	pos = 0
	sub_len = len(sub_str)
	

	while True:
		rs = ori_str.find(sub_str, pos)
		if(rs < 0):
			break

		pos_list.append((rs, sub_len))
		pos = rs+1

	return pos_list


def output_content(content, org_info_list):

	#print("++++++++++++++++++++++++")
	#print(content)
	#print(org_info_list)
	#print("++++++++++++++++++++++++")

	# init content
	content_ch_list = []

	for i in range(len(content)):
		content_ch_list.append((content[i], 'O'))

	for i in range(len(org_info_list)):
		(pos, org_len) = org_info_list[i]

		is_replace = True

		for j in range(pos, pos+org_len):
			if('O' != content_ch_list[j][1]):
				is_replace = False

#		print("++++++")
#		print(is_replace)

		if True == is_replace:
			for j in range(pos, pos+org_len):
				(ch, label) = content_ch_list[j]

				if j == pos:
					content_ch_list[j] = (ch, 'B-ORG')
				else:
					content_ch_list[j] = (ch, 'I-ORG')

	for i in range(len(content_ch_list)):
		(ch, label) = content_ch_list[i]

		print("%s %s" % (ch, label))

	print("")




#for line in open("news_sample", "rb"):
for line in open("news_sample", "r"):
	line = line.strip()
	#print(line)
	line_list = line.split('\1')

	#print("========================")
	#print(line_list[0])
	#print("========================")
	#print(line_list[1])
	#print("========================")

	#org_info_list = []

	if 2 == len(line_list):

		content_long = line_list[0]

		content_list = re.split('，|。|<p>|</p>', content_long)

		for j in range(len(content_list)):
			content = content_list[j]
			org_info_list = []

			if "" != content and "" != line_list[1]:

				org_list = line_list[1].split('\2', True)

				for i in range(len(org_list)):
					org = org_list[i]

					pos_list = find_str(content, org)

					org_info_list += pos_list

				output_content(content, org_info_list)

