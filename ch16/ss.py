# Replace urllib.request with urllib if you use Python 2.
# I would love to see a more elegant solution for this exercise, possibly by someone who understands html.

import urllib.request

def check(zip_code):
	if zip_code == 'done':
		return False
		
	else:
		if len(zip_code) != 5:
			print("\nThe zip code must have five digits!")
		return True

def get_html(zip_code):
	gibberish = urllib.request.urlopen('http://www.uszip.com/zip/' + zip_code)
	less_gib = gibberish.read().decode('utf-8')
	return less_gib

def extract_truth(code, key, delimiter):
	pos = code.find(key) + len(key)
	nearly_true = code[pos:pos+40]
	truth = nearly_true.split(delimiter)[0]
	return truth

while True:
	zip_code = input('Please type a zip code (5 digits) or "done" if want to stop:\n')
	
	if not check(zip_code):
                 break
	
	code = get_html(zip_code)
	
	invalid_key = '(0 results)'
	if invalid_key in code:
		print('\nNot a valid zip code.')
		continue
	
	name_key = '<title>'
	name_del = ' zip'
	name = extract_truth(code, name_key, name_del)
	
	pop_key = 'Total population</dt><dd>'
	pop_del = '<'
	pop = extract_truth(code, pop_key, pop_del)
	
	if not 1 < len(pop) < 9:
		pop = 'not available'

	print('\n' + name)
	print('Population:', pop, '\n')
