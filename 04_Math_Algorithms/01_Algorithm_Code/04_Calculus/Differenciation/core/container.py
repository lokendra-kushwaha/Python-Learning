def clean_expression(expression):
    ex1 = expression.replace('+ -', '- ')
    ex2 = ex1.replace(' + 0', '')

    return ex2

class Expression:
    
    def __init__(self, *args):
        self.element = args

    def __repr__(self):
        expression = ''
        for item in self.element:
            expression += f' + {str(item)}'.replace('+ -', '- ')
        
        return clean_expression(expression)
    
    def derive(self):
        
        new_exp = []
        for item in self.element:
            term = item.derive()

            new_exp.append(term)

        return Expression(*new_exp)