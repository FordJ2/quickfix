import language_tool_python, time

def main():
	def formal(x):
		yoshi = (x.lower())
		p4 = yoshi.replace("dont", "do not")
		p5 = p4.replace("youre", "you are")
		p6 = p5.replace("youll", "you will")
		p7 = p6.replace("youd", "you would")
		p8 = p7.replace("youve", "you have")
		p9 = p8.replace("hes", "he is")
		p11 = p9.replace("hed", "he would")
		p12 = p11.replace("shes", "she is")
		p14 = p12.replace("shed", "she would")
		p15 = p14.replace("its", "it is")
		p16 = p15.replace("itll", "it will")
		p17 = p16.replace("itd", "it would")
		p18 = p17.replace("were", "we are")
		p20 = p18.replace("wed", "we would")
		p21 = p20.replace("weve", "we have")
		p22 = p21.replace("wed", "we would")
		p23 = p22.replace("theyre", "they are")
		p24 = p23.replace("theyll", "they will")
		p25 = p24.replace("theyd", "they would")
		p26 = p25.replace("theyve", "they have")
		p27 = p26.replace("thats", "that is")
		p28 = p27.replace("thatll", "that will")
		p29 = p28.replace("thatd", "that would")
		p30 = p29.replace("whos", "who is")
		p31 = p30.replace("wholl", "who will")
		p32 = p31.replace("whod", "who would")
		p33 = p32.replace("whatre", "what are")
		p34 = p33.replace("whatll", "what will")
		p35 = p34.replace("whatd", "what would")
		p36 = p35.replace("whats", "what is")
		p37 = p36.replace("wheres", "where is")
		p38 = p37.replace("wherell", "where will")
		p39 = p38.replace("whered", "where would")
		p40 = p39.replace("whens", "when is")
		p41 = p40.replace("whenll", "when will")
		p42 = p41.replace("whend", "when would")
		p43 = p42.replace("whys", "why is")
		p44 = p43.replace("whyll", "why will")
		p45 = p44.replace("whyd", "why would")
		p46 = p45.replace("howll", "how will")
		p47 = p46.replace("howd", "how would")
		p48 = p47.replace("hows", "how is")
		p49 = p48.replace("you're", "you are")
		p50 = p49.replace("you'll", "you will")
		p51 = p50.replace("you'd", "you would")
		p52 = p51.replace("you've", "you have")
		p53 = p52.replace("he's", "he is")
		p54 = p53.replace("he'll", "he will")
		p55 = p54.replace("he'd", "he would")
		p56 = p55.replace("she's", "she is")
		p57 = p56.replace("she'll", "she will")
		p58 = p57.replace("she'd", "she would")
		p59 = p58.replace("it's", "it is")
		p60 = p59.replace("it'll", "it will")
		p61 = p60.replace("it'd", "it would")
		p62 = p61.replace("we're", "we are")
		p63 = p62.replace("we'll", "we will")
		p64 = p63.replace("we've", "we have")
		p65 = p64.replace("we'd", "we would")
		p66 = p65.replace("they're", "they are")
		p67 = p66.replace("they'll", "they will")
		p68 = p67.replace("they'd", "they would")
		p69 = p68.replace("they've", "they have")
		p70 = p69.replace("that's", "that is")
		p71 = p70.replace("that'll", "that will")
		p72 = p71.replace("that'd", "that would")
		p73 = p72.replace("who's", "who is")
		p74 = p73.replace("who'll", "who will")
		p75 = p74.replace("who'd", "who would")
		p76 = p75.replace("what's", "what is")
		p77 = p76.replace("what're", "what are")
		p78 = p77.replace("what'll", "what will")
		p79 = p78.replace("what'd", "what would")
		p80 = p79.replace("where's", "where is")
		p81 = p80.replace("where'll", "where will")
		p82 = p81.replace("where'd", "where would")
		p83 = p82.replace("when's", "when is")
		p84 = p83.replace("when'll", "when will")
		p85 = p84.replace("when'd", "when would")
		p86 = p85.replace("why's", "why is")
		p87 = p86.replace("why'll", "why will")
		p88 = p87.replace("why'd", "why would")
		p89 = p88.replace("how'll", "how will")
		p90 = p89.replace("how'd", "how would")
		p91 = p90.replace("how's", "how is")
		i1 = p91.lower().replace(' i ', ' I ')
		i2 = i1.replace(' i.', ' I.')
		i3 = i2.replace(' i!', ' I!')
		i4 = i3.replace(' i?', ' I?')
		i5 = i4.replace(' im ', 'Im')
		i7 = i5.replace("id", "Id")
		i8 = i7.replace("ive", "Ive")
		i9 = i8.replace(" i'm ", "I am")
		i10 = i9.replace("i'll", "I will")
		i11 = i10.replace("i'd", "I would")
		ok = i11.replace("i've", "I have")
		return ok

	def capDot(x):
		r1 = x.replace('. a', '. A')
		r1 = r1.replace('. b', '. B')
		r1 = r1.replace('. c', '. C')
		r1 = r1.replace('. d', '. D')
		r1 = r1.replace('. e', '. E')
		r1 = r1.replace('. f', '. F')
		r1 = r1.replace('. g', '. G')
		r1 = r1.replace('. h', '. H')
		r1 = r1.replace('. i', '. I')
		r1 = r1.replace('. j', '. J')
		r1 = r1.replace('. k', '. K')
		r1 = r1.replace('. l', '. L')
		r1 = r1.replace('. m', '. M')
		r1 = r1.replace('. n', '. N')
		r1 = r1.replace('. o', '. O')
		r1 = r1.replace('. p', '. P')
		r1 = r1.replace('. q', '. Q')
		r1 = r1.replace('. r', '. R')
		r1 = r1.replace('. s', '. S')
		r1 = r1.replace('. t', '. T')
		r1 = r1.replace('. u', '. U')
		r1 = r1.replace('. v', '. V')
		r1 = r1.replace('. w', '. W')
		r1 = r1.replace('. x', '. X')
		r1 = r1.replace('. y', '. Y')
		r1 = r1.replace('. z', '. Z')
		r1 = r1.replace('! a', '! A')
		r1 = r1.replace('! b', '! B')
		r1 = r1.replace('! c', '! C')
		r1 = r1.replace('! d', '! D')
		r1 = r1.replace('! e', '! E')
		r1 = r1.replace('! f', '! F')
		r1 = r1.replace('! g', '! G')
		r1 = r1.replace('! h', '! H')
		r1 = r1.replace('! i', '! I')
		r1 = r1.replace('! j', '! J')
		r1 = r1.replace('! k', '! K')
		r1 = r1.replace('! l', '! L')
		r1 = r1.replace('! m', '! M')
		r1 = r1.replace('! n', '! N')
		r1 = r1.replace('! o', '! O')
		r1 = r1.replace('! p', '! P')
		r1 = r1.replace('! q', '! Q')
		r1 = r1.replace('! r', '! R')
		r1 = r1.replace('! s', '! S')
		r1 = r1.replace('! t', '! T')
		r1 = r1.replace('! u', '! U')
		r1 = r1.replace('! v', '! V')
		r1 = r1.replace('! w', '! W')
		r1 = r1.replace('! x', '! X')
		r1 = r1.replace('! y', '! Y')
		r1 = r1.replace('! z', '! Z')
		r1 = r1.replace('? a', '? A')
		r1 = r1.replace('? b', '? B')
		r1 = r1.replace('? c', '? C')
		r1 = r1.replace('? d', '? D')
		r1 = r1.replace('? e', '? E')
		r1 = r1.replace('? f', '? F')
		r1 = r1.replace('? g', '? G')
		r1 = r1.replace('? h', '? H')
		r1 = r1.replace('? i', '? I')
		r1 = r1.replace('? j', '? J')
		r1 = r1.replace('? k', '? K')
		r1 = r1.replace('? l', '? L')
		r1 = r1.replace('? m', '? M')
		r1 = r1.replace('? n', '? N')
		r1 = r1.replace('? o', '? O')
		r1 = r1.replace('? p', '? P')
		r1 = r1.replace('? q', '? Q')
		r1 = r1.replace('? r', '? R')
		r1 = r1.replace('? s', '? S')
		r1 = r1.replace('? t', '? T')
		r1 = r1.replace('? u', '? U')
		r1 = r1.replace('? v', '? V')
		r1 = r1.replace('? w', '? W')
		r1 = r1.replace('? x', '? X')
		r1 = r1.replace('? y', '? Y')
		dot1 = r1.replace('? z', '? Z')
		return dot1

	def informal(x):
		yoshi = (x.lower())
		c1 = yoshi.replace("dont", "don't")
		c2 = c1.replace("isnt", "isn't")
		c3 = c2.replace("howd", "how'd")
		c4 = c3.replace("youre", "you're")
		c5 = c4.replace("youll", "you'll")
		c6 = c5.replace("youd", "you'd")
		c7 = c6.replace("youve", "you've")
		c8 = c7.replace("hes", "he's")
		c9 = c8.replace("hed", "he'd")
		c10 = c9.replace("shes", "she's")
		c11 = c10.replace("shed", "she'd")
		c12 = c11.replace("itll", "it'll")
		c13 = c12.replace("itd", "it'd")
		c14 = c13.replace("wed", "we'd")
		c15 = c14.replace("weve", "we've")
		c16 = c15.replace("theyre", "they're")
		c17 = c16.replace("theyll", "they'll")
		c18 = c17.replace("theyd", "they'd")
		c19 = c18.replace("theyve", "they've")
		c20 = c19.replace("thats", "that's")
		c21 = c20.replace("thatll", "that'll")
		c22 = c21.replace("thatd", "that'd")
		c23 = c22.replace("whos", "who's")
		c24 = c23.replace("wholl", "who'll")
		c25 = c24.replace("whod", "who'd")
		c26 = c25.replace("whats", "what's")
		c27 = c26.replace("whatre", "what're")
		c28 = c27.replace("whatll", "what'll")
		c29 = c28.replace("whatd", "what'd")
		c30 = c29.replace("whats", "what's")
		c31 = c30.replace("wheres", "where's")
		c32 = c31.replace("wherell", "where'll")
		c33 = c32.replace("whered", "where'd")
		c34 = c33.replace("hows", "how's")
		c35 = c34.replace("whens", "when's")
		c36 = c35.replace("whenll", "when'll")
		c37 = c36.replace("whend", "when'd")
		c38 = c37.replace("whys", "why's")
		c39 = c38.replace("whyll", "why'll")
		c40 = c39.replace("whyd", "why'd")
		c41 = c40.replace("howll", "how'll")
		c42 = c41.replace("Im", "I'm")
		c43 = c42.replace("Id", "I'd")
		output5 = c43.replace("Ive", "I've")
		return output5

	def grammar(x):
		text = x
		tool = language_tool_python.LanguageTool('en-US')
		matches = tool.check(text)
		matches
		my_mistakes = []
		my_corrections = []
		start_positions = []
		end_positions = []
		for rules in matches:
			if len(rules.replacements)>0:
				start_positions.append(rules.offset)
				end_positions.append(rules.errorLength+rules.offset)
				my_mistakes.append(text[rules.offset:rules.errorLength+rules.offset])
				my_corrections.append(rules.replacements[0])
		my_new_text = list(text)
		for m in range(len(start_positions)):
			for i in range(len(text)):
				my_new_text[start_positions[m]] = my_corrections[m]
				if (i>start_positions[m] and i<end_positions[m]):
					my_new_text[i]=""
		newtext = "".join(my_new_text)
		return newtext

	name = ('quickfix'.upper())

	print(
		f'''
		{name} 2.0.0
		Copyright (c) 2021 Jonathan Ford
		Licensed under the GNU AGPL 3.0
		'''
	)

	userSTR = str(input(':\nWhat sentences would you like to edit? (paste below) \n-->'))

	userBLNK = userSTR.replace(' ', '')
	letterCount = len(userBLNK)
	wordCount = len(userSTR.split())

	time.sleep(0.5)
	print(f'\n:    :\nYour letter count is at:\n{letterCount}')

	time.sleep(0.5)
	print(f'\n:    :\nYour word count is at:\n{str(wordCount)}')

	check = [
		"were",
		"well",
		"its",
		"shell",
		"hell",
		"ill",
		"lets",
		"id"
	]

	time.sleep(1)
	print('\n\nWhat would you like to do with your sentences?')

	time.sleep(1)
	print(':    :    :\nSelect a letter:')

	time.sleep(1)
	choice = input(
		f'''
		a) Fix up spelling and grammar to the best of {name}'s abilities (does everything in its power to fix up your sentences)
		b) Choose what to do, with a multitude of custom options
		-->'''
	)


	#instant
	if choice.strip().lower() == 'a':
		time.sleep(1)
		print('\nIs this for a formal application?')
		formal = input('Yes or No\n-->')

		#formal
		if formal.strip().lower() == 'yes' or formal.strip().lower() == 'y':
			time.sleep(1)

			newtext = grammar(userSTR)
			
			output1 = newtext.replace('. ', ' . ').replace('! ', ' ! ').replace('? ', ' ? ')

			output2 = (formal(output1))

			if any(word in output2 for word in check):
				print(f'\nPlease review words like:\n{check}')

			yes2 = output2.capitalize().replace(' . ', '. ').replace(' ! ', '! ').replace(' ? ', '? ')

			dot1 = capDot(yes2)

			if dot1.strip().lower().endswith('.'):
				time.sleep(1)
				print(f'\n:    :    :    :\nYour final output is:\n{dot1}\n')
			
			else:
				time.sleep(1)
				print(f'\n:    :    :    :\nYour final output is:\n{dot1}.\n')

		#informal
		else:
			time.sleep(1)

			newtext = grammar(userSTR)
			
			output3 = newtext.replace('. ', ' . ').replace('! ', ' ! ').replace('? ', ' ? ')

			output4 = informal(output3)

			if any(word in output4 for word in check):
				time.sleep(1)
				print(f'\nPlease review words like:\n{check}')

			yes2 = output4.capitalize().replace(' . ', '. ').replace(' ! ', '! ').replace(' ? ', '? ')

			dot2 = capDot(yes2)
			
			if dot2.strip().lower().endswith('.'):
				time.sleep(1)
				print(f'\n:    :    :    :\nYour final output is:\n{dot2}\n')
			
			else:
				time.sleep(1)
				print(f'\n:    :    :    :\nYour final output is:\n{dot2}.\n')

	#custom
	elif choice.strip().lower() == 'b':
		time.sleep(1)
		print('\n:    :    :\nSelect a letter:')
		action = input(
			'''
			a) MAKE EVERYTHING UPERCASE
			b) make everything lowercase
			c) Capitalize. The. First. Letter.
			d) Capitalize I's
			e) Contract contractions
			f) Expand contractions - formal
			g) E x p a n d
			h) R_plac_ l_tt_rs or words
			i) Fix spelling and grammar
			j) exit
			--> ''')

		#uppercase
		if action.strip().lower() == 'a':
			time.sleep(1)
			print(f'\n:    :    :    :\nYour final output is:\n{userSTR.upper()}\n')

		#lowercase
		elif action.strip().lower() == 'b':
			time.sleep(1)
			print(f'\n:    :    :    :\nYour final output is:\n{userSTR.lower()}\n)')

		#capitalize sentences 
		elif action.strip().lower() == 'c':
			yes2 = userSTR.capitalize().replace(' . ', '. ').replace(' ! ', '! ').replace(' ? ', '? ')

			dot3 = capDot(yes2)

			if dot3.strip().lower().endswith('.'):
				time.sleep(1)
				print(f'\n:    :    :    :\nYour final output is:\n{dot3}\n')
			
			else:
				time.sleep(1)
				print(f'\n:    :    :    :\nYour final output is:\n{dot3}.\n')

		#capitalize I's
		elif action.strip().lower() == 'd': 
			i1 = userSTR.replace(' i ', ' I ')
			i2 = i1.replace(' i.', ' I.')
			i3 = i2.replace(' i!', ' I!')
			i4 = i3.replace(' i?', ' I?')
			i5 = i4.replace(' im ', 'Im') 
			i6 = i5.replace("ill", "Ill")
			i7 = i6.replace("id", "Id")
			toad = i7.replace("ive", "Ive")
			
			time.sleep(1)
			print(f'\n:    :    :    :\nYour final output is:\n{toad}\n')

		#contractions
		elif action.strip().lower() == 'e':
			output5 = informal(userSTR)

			if any(word in output5 for word in check):
				time.sleep(1)
				print(f'\nPlease review words like:\n{check}')

			yes2 = output5.capitalize().replace(' . ', '. ').replace(' ! ', '! ').replace(' ? ', '? ')

			dot4 = capDot(yes2)

			if dot4.strip().lower().endswith('.'):
				time.sleep(1)
				print(f'\n:    :    :    :\nYour final output is:\n{dot4}\n')
			
			else:
				time.sleep(1)
				print(f'\n:    :    :    :\nYour final output is:\n{dot4}.\n')

		#expand contraction
		elif action.strip().lower() == 'f':
			
			output6 = (formal(userSTR))
			
			if any(word in output6 for word in check):
				time.sleep(1)
				print(f'\nPlease review words like:\n{check}')

			yes2 = output6.capitalize().replace(' . ', '. ').replace(' ! ', '! ').replace(' ? ', '? ')

			dot5 = capDot(yes2)

			if dot5.strip().lower().endswith('.'):
				time.sleep(1)
				print(f'\n:    :    :    :\nYour final output is:\n{dot5}\n')
			
			else:
				time.sleep(1)
				print(f'\n:    :    :    :\nYour final output is:\n{dot5}.\n')

		#e x p a n d
		elif action.strip().lower() == 'g':
			time.sleep(1)
			print(f"\n:    :    :    :\n{' '.join(userSTR)}\n")

		#replace
		elif action.strip().lower() == 'h':
			time.sleep(1)
			before = input('\n:    :    :    :\nWhat word would you like to replace?\n-->')
			time.sleep(1)
			after = input('\n:    :    :    :\nWhat word would you like to put instead?\n-->')
			time.sleep(1)
			print(f'\n:    :    :    :\nYour final output is:\n{userSTR.replace(before, after)}\n')
			
		#spelling
		elif action.strip().lower() == 'i':
			time.sleep(1)

			newtext = grammar(userSTR)

			userSTR = newtext

			print(f'\n:    :    :    :\nYour final output is:\n{userSTR}\n')

		#exit
		elif action.strip().lower() == 'j' or action.strip().lower() == 'exit':
			time.sleep(1)
			print('\n:    :    :    :\nGoodbye!\n')

		#error
		else:
			time.sleep(1)
			print(':    :    :    :\nSelect a valid letter next time :)')

		#rerun
		time.sleep(1)
		print(f'\nWould you like to run {name} again?')
		time.sleep(0.5)
		repeat = input('Yes or No\n-->')

		if repeat.strip().lower() == 'yes' or repeat.strip().lower() == 'y':

			#intro input
			time.sleep(1.5)
			rep = input('\n\nWould you like to use a new set of sentences?\n\nYes or No ——>')

			if rep.strip().lower() == 'y' or rep.strip().lower() == 'ye' or rep.strip().lower() == 'yes':
				time.sleep(1)
				print(f'\nDon\'t forget to copy {name} so you dont loose it\n')
			
			else:
				time.sleep(1)
				print(f'\nPlease copy your current text and relaunch {name}\n')

		else:
			print('')

	#feedback
	time.sleep(1)
	print (f'\n\n:    :    :    :    :\nWould you like to send in feedback on {name}\n')
	feedback = input('Yes or No\n-->')

	#email
	if feedback.strip().lower() == 'yes' or feedback.strip().lower() == 'y' or feedback.strip().lower() == 'ye' or feedback.strip().lower() == 'ya':
		time.sleep(1)
		print('\n:    :    :    :    :\nPlease submit your feedback in the github repository:\nhttps://github.com/wncry/quickfix/issues\n')

		time.sleep(1)
		print(f'\n:    :    :    :    :    :\nThank you for your time!\n\nIf you would ever like to use {name} again, just reopen the app.\n\nヽ(•‿ •)ノ\n')

	#exit
	else:
		time.sleep(1)
		print(f'\n:    :    :    :    :    :\nThank you for your time!\n\nIf you would ever like to use {name} again, just reopen the app.\n\nヽ(•‿ •)ノ\n')

	print('\n\n')

	print('Closing in:')
	for i in range(15):
		print(i)
		time.sleep(1)

if __name__ == "__main__":
	main()
