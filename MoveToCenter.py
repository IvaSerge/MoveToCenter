import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)

import System
from System import Array
from System.Collections.Generic import *

import itertools
import math

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument
uidoc=DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

uiapp = DocumentManager.Instance.CurrentUIApplication
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
app = uiapp.Application

reLoad = IN[0]
selob = uidoc.Selection.PickObjects(
            Autodesk.Revit.UI.Selection.ObjectType.Element,
            "Selection of two elements")

if len(selob) != 2:
    raise ValueError("Only 2 elements need to be selected")

lastob = uidoc.Selection.PickObject(
            Autodesk.Revit.UI.Selection.ObjectType.Element,
            "Selection of two elements")

refList = list()
map(lambda x: refList.append(x), selob)
refList.append(lastob)

obList = list()
map(lambda x: obList.append(doc.GetElement(x.ElementId)), refList)

#new point coordinates calculation


OUT = obList