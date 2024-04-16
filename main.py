from Views.main import View
from Controllers.main import Main_Controller
from Model.main import Model
    
#Main
if __name__ == "__main__":
    view = View()
    model = Model()
    controller = Main_Controller(view, model)