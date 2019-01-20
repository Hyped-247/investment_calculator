from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError


style = style_from_dict({
	Token.QuestionMark: '#FCDB0A bold',
	Token.Selected: '#FCDB0A bold',
	Token.Instruction: '#FCDB0A bold',
	Token.Answer: '#FC0A0A bold',
	Token.Question: '#00FF22 bold',
})


class NumberValidator(Validator):
	
	def validate(self, document):
		try:
			int(document.text)
		except ValueError:
			raise ValidationError(
				message="Please enter an int.",
				cursor_position=len(document.text)
			)


questions = [
	{
		'type': 'input',
		'name': 'passive_income_desired_yearly',
		'message': 'How must passive income do you desire yearly?',
		'validate': NumberValidator
	},
{
		'type': 'input',
		'name': 'yearly_savings',
		'message': 'How much are you willing to invest every year?',
		'validate': NumberValidator
	},
{
		'type': 'input',
		'name': 'starting_year',
		'message': 'When are you going to start investing? ex. 2022',
		'validate': NumberValidator
	},
{
		'type': 'input',
		'name': 'price_of_one_apt',
		'message': 'What is the price for one apt?',
		'validate': NumberValidator
	},
{
		'type': 'input',
		'name': 'price_of_renting_one_apt',
		'message': 'How much does rent cost for one year?',
		'validate': NumberValidator
	},
]

if __name__ == "__main__":
	from investment_calculator import Calculator
	from pyfiglet import Figlet
	f = Figlet(font='slant')
	print(f.renderText("Real estate investment calculator"))
	answers = prompt(questions, style=style)
	passive_income_desired_yearly = int(answers.get('passive_income_desired_yearly'))
	yearly_savings = int(answers.get('yearly_savings'))
	starting_year = int(answers.get('starting_year'))
	price_of_one_apt = int(answers.get('price_of_one_apt'))
	price_of_renting_one_apt = int(answers.get('price_of_renting_one_apt'))
	object_calculator = Calculator(passive_income_desired_yearly,
	                               yearly_savings,starting_year,
	                               price_of_one_apt,
	                               price_of_renting_one_apt)
	object_calculator.print_results()
