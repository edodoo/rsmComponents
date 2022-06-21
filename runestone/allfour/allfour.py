#Components of a directive
#1.) Initialization
#2.) Parse Time
#3.) Output
#-------------------------
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive

#Parsing
class AllFourNode(nodes.General, nodes.Element):
    #Container to hold data until it is time to render output
    def __init__(self, content):
        super(AllFourNode, self).__init__()
        self.af_content = content

class AllFour(Directive):
    required_arguments = 0
    optional_arguments = 3
    has_content = True
    option_spec = {
        "items": directives.unchanged,
        "positions": directives.positive_int,
        "type": directives.positive_int
    }

    def run(self):
        env = self.state.document.settings.env

        if not hasattr(env, 'allfourcounter'):
            env.allfourcounter = 0
        env.allfourcounter += 1

        self.options["divid"] = self.arguments[0]
        if self.content: #specifies if a directive has content self.content is body content of directive
            source = "\n".join(self.content)
        else:
            source = "\n"
        self.options["filecontent"] = source

        url_str = "https://web.eecs.umich.edu/~mjguz/teaspoon/allfour/all-four-interactive-bootstrap-houghj.lc"

        if "items" not in self.options:
            return [nodes.raw('', f'<p align="center"><iframe src="{url_str}" width="110%" height="600px"></iframe></p>', format="html")]
        url_str += f"?elements={self.options['items']}"

        if "positions" not in self.options:
            self.options["positions"] = 0
        url_str += f"&k={self.options['positions']}"

        if "type" not in self.options or self.options["type"] < 0 or self.options["type"] > 4:
            self.options["type"] = 1
        url_str += f"&type={self.options['type']}"

        return [nodes.raw('', f'<p align="center"><iframe src="{url_str}" width="110%" height="600px"></iframe></p>', format="html")]

def setup(app):
    app.add_directive('allfour', AllFour)
    app.add_javascript('bookfuncs.js')
    app.add_javascript('skulpt/dist/skulpt.js')
    app.add_javascript('skulpt/dist/builtin.js')

    app.connect('doctree-resolved', process_allfour_nodes)
    app.connect('env-purge-doc', purge_allfours)

def process_allfour_nodes(arg1, arg2,arg3):
    pass

def purge_allfours(arg1, arg2, arg3):
    pass