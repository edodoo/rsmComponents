#Components of a directive
#1.) Initialization
#2.) Parse Time
#3.) Output
#-------------------------
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive

#Parsing
class ProgrammedCountingToolNode(nodes.General, nodes.Element):
    #Container to hold data until it is time to render output
    def __init__(self, content):
        super(ProgrammedCountingToolNode, self).__init__()
        self.pctool_content = content

class ProgrammedCountingTool(Directive):
    required_arguments = 0
    optional_arguments = 1
    has_content = True
    option_spec = {
        "example": directives.positive_int,
    }

    def run(self):
        env = self.state.document.settings.env

        if not hasattr(env, 'programmedcountingtoolcounter'):
            env.programmedcountingtoolcounter = 0
        env.programmedcountingtoolcounter += 1

        self.options["divid"] = self.arguments[0]
        if self.content: #specifies if a directive has content self.content is body content of directive
            source = "\n".join(self.content)
        else:
            source = "\n"
        self.options["filecontent"] = source

        url_str = "https://web.eecs.umich.edu/~mjguz/teaspoon/ProgrammedCounting/programmed-counting-interactive-houghj.lc"

        if "example" in self.options and 1 <= self.options['example'] <= 10:
            url_str += f"?example={self.options['example']}"

        return [nodes.raw('', f'<p align="center"><iframe src="{url_str}" width="110%" height="600px"></iframe></p>', format="html")]

def setup(app):
    app.add_directive('programmedcountingtool', ProgrammedCountingTool)
    app.add_javascript('bookfuncs.js')
    app.add_javascript('skulpt/dist/skulpt.js')
    app.add_javascript('skulpt/dist/builtin.js')

    app.connect('doctree-resolved', process_programmedcountingtool_nodes)
    app.connect('env-purge-doc', purge_programmedcountingtools)

def process_programmedcountingtool_nodes(arg1, arg2,arg3):
    pass

def purge_programmedcountingtools(arg1, arg2, arg3):
    pass