
lesson =['Lesson 1:Basics of the World Wide Web and HTML', 'Lesson 2:Creating a Structured Document with HTML', 'Patty Cakes',
'Lesson 3:Adding Style to Structure with CSS', 'Lesson 4:Introduction to "Serious" Programming', 'Lesson 5:Variables and Strings', 
'Lesson 6:Input-> Function-> Output','Lesson 7:Decisions and Repetition: If and While','Lesson 8:Structured Data- Lists and For Loops']



concept_title = ['Major Pieces of the Internet Include:', 'Hypertext Markup Language (HTML)-"The Heart of the Web"', 'Patty Cakes',
'Derri Anne Connecticut', 'Moe Dess', 'Leda Doggslife', 'Dan Druff',
'Al Fresco', 'Ido Hoe', 'Howie Kisses', 'Len Lease', 'Phil Meup',
'Ira Pent', 'Ben D. Rules', 'Ave Sectomy', 'Gary Shattire',
'Bobbi Soks', 'Sheila Takya', 'Rose Tattoo', 'Moe Tell']

concept_description =  ['$29.95', '$8.37', '$15.26', '$19.25', '$19.25',
'$13.99', '$31.57', '$8.49', '$14.47', '$15.86', '$11.11',
'$15.98', '$16.27', '$7.50', '$50.85', '$14.26', '$5.68',
'$15.00', '$114.07', '$10.09']


def build_me_my_html(concept_title, concept_description):
	html_text_1 = '''
	<div class="concept">
		<div class = "concept-title">
			''' + concept_title
	html_text_2 = '''
		</div>
		<div class="concept-description">
			''' + concept_description
	html_text_3 = '''
		</div>
	</div>'''

	full_html_text= html_text_1 + html_text_2 + html_text_3
	return full_html_text


first_concept= 'CSS'
first_description= 'CSS Stands for...'

print build_me_my_html(first_concept, first_description)
	
