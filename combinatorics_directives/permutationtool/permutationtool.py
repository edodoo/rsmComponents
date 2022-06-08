#Components of a directive
#1.) Initialization
#2.) Parse Time
#3.) Output
#-------------------------
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive

#Parsing
class PermutationToolNode(nodes.General, nodes.Element):
    #Container to hold data until it is time to render output
    def __init__(self, content):
        super(PermutationToolNode, self).__init__()
        self.pmt_content = content

class PermutationTool(Directive): #One class for every directive
    required_arguments = 0 #specifies how many arguments a directive can take
    optional_arguments = 10
    option_spec = {
        "num1": directives.positive_int,
        "num2": directives.positive_int,
        "num3": directives.positive_int,
        "num4": directives.positive_int,
        "num5": directives.positive_int,
        "element1": directives.unchanged,
        "element2": directives.unchanged,
        "element3": directives.unchanged,
        "element4": directives.unchanged,
        "element5": directives.unchanged
    }

    def run(self):
        env = self.state.document.settings.env

        if not hasattr(env, 'permutationtoolcounter'):
            env.permutationtoolcounter = 0
        env.permutationtoolcounter += 1

        self.options["divid"] = self.arguments[0]
        if self.content:
            source = "\n".join(self.content)
        else:
            source ="\n"
        self.options["filecontent"] = source

        url_str = "https://web.eecs.umich.edu/~mjguz/teaspoon/Permutations/permutations-angelai.lc"
        first = True #Boolean used to check for first option to be added to query
        for n in range(1, 6):
            num_str = "num" + str(n)
            el_str = "element" + str(n)
            if num_str in self.options and el_str in self.options:
                if first:
                        url_str += f"?number{n}={self.options[num_str]}&element{n}={self.options[el_str]}" #Start the query on the first option
                        first = False
                else:
                    url_str += f"&number{n}={self.options[num_str]}&element{n}={self.options[el_str]}"

        return [nodes.raw('', f'<p align="center"><iframe src="{url_str}" width="100%" height="600px"></iframe></p>', format="html")] #Must return a list of nodes

#Initialization
def setup(app):
    app.add_directive('permutationtool', PermutationTool) #maps permuatationtool directive to PermuationTool class
    app.add_javascript('bookfuncs.js') #jst files we want to include
    app.add_javascript('skulpt/dist/skulpt.js')
    app.add_javascript('skulpt/dist/builtin.js')

    app.connect('doctree-resolved', process_permutationtool_nodes)
    app.connect('env-purge-doc', purge_permutationtools)

def process_permutationtool_nodes(arg1, arg2, arg3):
    pass
def purge_permutationtools(arg1, arg2, arg3):
    pass
