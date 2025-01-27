from gtep.gtep_model_cho import ExpansionPlanningModelwithReliability
from gtep.gtep_model import ExpansionPlanningModel
from gtep.gtep_data_cho import ExpansionPlanningData
from gtep.gtep_solution import ExpansionPlanningSolution
from gtep.gtep_solution_cho import ExpansionPlanningSolutionwithReliability
from pyomo.core import TransformationFactory
from pyomo.contrib.appsi.solvers.highs import Highs
from pyomo.contrib.appsi.solvers.gurobi import Gurobi
import gurobipy as gp
from pyomo.environ import value, Param, Var
from pyomo.opt import SolverFactory
import csv


data_path = "./gtep/data/5bus"
data_object = ExpansionPlanningData()
data_object.load_prescient(data_path)

mod_object = ExpansionPlanningModelwithReliability(
    stages=2,
    data=data_object.md,
    num_reps=2,
    len_reps=1,
    num_commit=6,
    num_dispatch=4,
)
mod_object.create_model()
TransformationFactory("gdp.bound_pretransformation").apply_to(mod_object.model)
TransformationFactory("gdp.bigm").apply_to(mod_object.model)
# opt = SolverFactory("gurobi")
# opt = Gurobi()
opt = Highs()
# # mod_object.results = opt.solve(mod_object.model, tee=True)
mod_object.results = opt.solve(mod_object.model)







pass
