#Components of a directive
#1.) Initialization
#2.) Parse Time
#3.) Output
#-------------------------
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive

#Parsing
class CountingSheetNode(nodes.General, nodes.Element):
    #Container to hold data until it is time to render output
    def __init__(self, content):
        super(CoutningSheetNode, self).__init__()
        self.cs_content = content

class CountingSheet(Directive):
    required_arguments = 0
    optional_arguments = 11
    has_content = True
    option_spec = {
        "ncols": directives.positive_int,
        "col1": directives.unchanged,
        "col2": directives.unchanged,
        "col3": directives.unchanged,
        "col4": directives.unchanged,
        "col5": directives.unchanged,
        "col6": directives.unchanged,
        "col7": directives.unchanged,
        "col8": directives.unchanged,
        "col9": directives.unchanged,
        "col10": directives.unchanged
    }

    def run(self):
        env = self.state.document.settings.env

        if not hasattr(env, 'countingsheetcounter'):
            env.countingsheetcounter = 0
        env.countingsheetcounter += 1

        self.options["divid"] = self.arguments[0]
        if self.content: #specifies if a directive has content self.content is body content of directive
            source = "\n".join(self.content)
        else:
            source = "\n"
        self.options["filecontent"] = source

        url_str = f"https://web.eecs.umich.edu/~mjguz/teaspoon/CountingSheet/counting-sheet-interactive-bootstrap-houghj.lc"

        if "ncols" not in self.options:
            self.options["ncols"] = 10
        url_str += f"?ncols={self.options['ncols']}"

        for i in range(1, self.options["ncols"] + 1):
            col_str = 'col' + str(i)
            if col_str in self.options:
                url_str += f"&{col_str}={self.options[col_str]}"


        return [nodes.raw('', f'<p align="center"><iframe src="{url_str}" width="110%" height="600px"></iframe></p>', format="html")]

def setup(app):
    app.add_directive('countingsheet', CountingSheet)
    app.add_javascript('bookfuncs.js')
    app.add_javascript('skulpt/dist/skulpt.js')
    app.add_javascript('skulpt/dist/builtin.js')

    app.connect('doctree-resolved', process_countingsheet_nodes)
    app.connect('env-purge-doc', purge_countingsheets)

def process_countingsheet_nodes(arg1, arg2,arg3):
    pass

def purge_countingsheets(arg1, arg2, arg3):
    pass