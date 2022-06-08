#Components of a directive
#1.) Initialization
#2.) Parse Time
#3.) Output
#-------------------------
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive

#Parsing
class AnalysisToolNode(nodes.General, nodes.Element):
    #Container to hold data until it is time to render output
    def __init__(self, content):
        super(AnalysisToolNode, self).__init__()
        self.atool_content = content

#Output
class AnalysisTool(Directive):
    required_arguments = 0
    optional_arguments = 2
    has_content = True
    option_spec = {
        "hide": directives.flag, #specifies which arguments a directive can take
        "edit": directives.flag,
    }

    def run(self):
        env = self.state.document.settings.env

        if not hasattr(env, 'analysistoolcounter'):
            env.analysistoolcounter = 0
        env.analysistoolcounter += 1

        self.options["divid"] = self.arguments[0]
        if self.content: #specifies if a directive has content self.content is body content of directive
            source = "\n".join(self.content)
        else:
            source = "\n"
        self.options["filecontent"] = source

        if "hide" not in self.options:
            self.options["hide"] = "block"
        else:
            self.options["hide"] = "none"

        if "edit" not in self.options:
            self.options["edit"] = False

        return [nodes.raw('', '<p align="center"><iframe src="https://web.eecs.umich.edu/~mjguz/teaspoon/AnalysisTools/analysis-tools-angelai.lc" width="110%" height="600px"></iframe></p>', format="html")]

#Initialization
def setup(app):
    app.add_directive('analysistool', AnalysisTool)
    app.add_javascript('bookfuncs.js')
    app.add_javascript('skulpt/dist/skulpt.js')
    app.add_javascript('skulpt/dist/builtin.js')

    app.connect('doctree-resolved', process_analysistool_nodes)
    app.connect('env-purge-doc', purge_analysistools)

def process_analysistool_nodes(arg1, arg2,arg3):
    pass

def purge_analysistools(arg1, arg2, arg3):
    pass