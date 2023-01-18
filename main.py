from module.model import Topsis

topsis = Topsis(["description", "degrees", "coresearchers", "major", "degree", "no_researchers", "no_awards"])
topsis.caculate_weight(["description", "degrees", "coresearchers", "major", "degree", "no_researchers", "no_awards"])