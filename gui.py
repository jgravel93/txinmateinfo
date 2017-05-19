from inmatesearch import *
from ipywidgets import *
from ipywidgets import widgets
from IPython.display import display

pd.set_option("display.max_columns",14)
input_form = """
<div style="border:solid navy; padding:20px;">
<div id="drop_zone">Drop files here</div>
<output id="list"></output>

"""
##<input type="file" id="file_selector" name="files[]"/>
##<output id="list"></output>
##</div>
##"""

javascript = """
<script>
  function handleFileSelect(evt) {
    evt.stopPropagation();
    evt.preventDefault();


    var files = evt.dataTransfer.files; // FileList object.

    // files is a FileList of File objects. List some properties.
    var output = [];
    for (var i = 0, f; f = files[i]; i++) {
      output.push('<li><strong>', escape(f.name), '</strong> (', f.type || 'n/a', ') - ',
                  f.size, ' bytes, last modified: ',
                  f.lastModifiedDate ? f.lastModifiedDate.toLocaleDateString() : 'n/a',
                  '</li>');
    }
    var reader = new FileReader();

      // Closure to capture the file information.
      reader.onload = (function(theFile) {
        return function(e) {
          // Render thumbnail.
          var span = document.createElement('span');
          span.innerHTML = ['<img class="thumb" src="', e.target.result,
                            '" title="', escape(theFile.name), '"/>'].join('');
          document.getElementById('list').insertBefore(span, null);
        };
      })(f);

      // Read in the image file as a data URL.
      reader.readAsDataURL(f);
    }
  }
    document.getElementById('list').innerHTML = '<ul>' + output.join('') + '</ul>';
  }
  function handleDragOver(evt) {
    evt.stopPropagation();
    evt.preventDefault();
    evt.dataTransfer.dropEffect = 'copy'; // Explicitly show this is a copy.
  }

  // Setup the dnd listeners.
  var dropZone = document.getElementById('drop_zone');
  dropZone.addEventListener('dragover', handleDragOver, false);
  dropZone.addEventListener('drop', handleFileSelect, false);
</script>
"""
##"""
##<script type="text/Javascript">
##  function handleFileSelect(evt) {
##    var kernel = IPython.notebook.kernel;
##    var files = evt.target.files; // FileList object
##    console.log('Executing orig')
##    console.log(files)
##    // files is a FileList of File objects. List some properties.
##    var output = [];
##    var f = files[0]
##    output.push('<li><strong>', escape(f.name), '</strong> (', f.type || 'n/a', ') - ',
##                  f.size, ' bytes, last modified: ',
##                  f.lastModifiedDate ? f.lastModifiedDate.toLocaleDateString() : 'n/a',
##                  '</_Mli>');
##    document.getElementById('list').innerHTML = '<ul>' + output.join('') + '</ul>';
##    var command = 'fname = "' + f.name + '"'
##    console.log(command)
##    kernel.execute(command);
##  }
##
##  document.getElementById('file_selector').addEventListener('change', handleFileSelect, false);
##</script>
##"""


def file_selector():
    from IPython.display import HTML, display
    display(HTML(input_form + javascript))

filepath='sid.csv'
header=None
names=["SID"]
idfield="SID"
savepath=None   
    

def displaytable(table):
    dt=table[['SID Number',
     'TDCJ Number',
     'Name',
     'Race',
     'Gender',
     'DOB',
     'Maximum Sentence Date',
     'Current Facility',
     'Projected Release Date',]].head(6)
    print('Output for the first 9 variables (criminal history is hidden) and 6 first cases')
    return print(dt)
def getTestTable():
    table=getInmateInfo(filepath=filepath,header=header,names=names, idfield=idfield,savepath=savepath)
    return table
def getOwnTable(df):
    table=getInmateInfoList(df)
    return table
def getFilePath():
    filepath=file_selector()
    return filepath
def openOwnTable(filepath):
    df=pd.read_csv(filepath, header=None, names=['SID'])
    cols=df.columns.values.tolist()
    
    return df
def saveOutput(df,savepath):
    df.to_csv(savepath, sep='  ')

button = widgets.Button(description="Test Data")

def on_button_clicked(b):
    print('Loading....')
    table=getTestTable()
    
    return displaytable(table)

sidtext=widgets.Text(
    description='SID:',
    disabled=False
)
def handle_submit(sender):
    print('Loading....')
    table=getInmateInfoNum(sidtext.value)
    
    return displaytable(table)

pathtext=widgets.Text(
    description='File path:',
    disabled=False
)
def handle_submit2(sender):
    print('Loading....')
    df=openOwnTable(pathtext.value)
    table=getOwnTable(df)
    return displaytable(table)
button.on_click(on_button_clicked)
sidtext.on_submit(handle_submit)
pathtext.on_submit(handle_submit2)

def main():
    
    accordion = widgets.Accordion(children=[button,sidtext,pathtext ])
    accordion.set_title(0, 'Use Test Data')
    accordion.set_title(1, 'Use SID')
    accordion.set_title(2, 'Use Own Data')
    return accordion
