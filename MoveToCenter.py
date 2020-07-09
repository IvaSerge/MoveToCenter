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

def ft_to_mm(ft):
	return ft*304.8

uiapp = DocumentManager.Instance.CurrentUIApplication
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
app = uiapp.Application

reLoad = IN[0]

Ob1 = uidoc.Selection.PickObject(
            Autodesk.Revit.UI.Selection.ObjectType.Element,
            "Selection of two elements")

Ob2 = uidoc.Selection.PickObject(
            Autodesk.Revit.UI.Selection.ObjectType.Element,
            "Selection of two elements")

selob = list()
selob.append(Ob1)
selob.append(Ob2)

lastob = uidoc.Selection.PickObject(
            Autodesk.Revit.UI.Selection.ObjectType.Element,
            "Selection of two elements")

refList = list()
map(lambda x: refList.append(x), selob)
refList.append(lastob)

obList = list()
map(lambda x: obList.append(doc.GetElement(x.ElementId)), refList)

#new point coordinates calculation
midPointX = (obList[0].Location.Point.X
           + obList[1].Location.Point.X)/2
midPointY =(obList[0].Location.Point.Y
           + obList[1].Location.Point.Y)/2

vectorX = midPointX - obList[2].Location.Point.X
vectorY = midPointY - obList[2].Location.Point.Y
midPointXYZ = XYZ(vectorX, vectorY , 0)

#move element
TransactionManager.Instance.EnsureInTransaction(doc)
ElementTransformUtils.MoveElement(doc,  obList[2].Id, midPointXYZ)
TransactionManager.Instance.TransactionTaskDone()