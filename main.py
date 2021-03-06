from functions.data_functions import get_input_data
from functions.model_functions import run_SEIR_ODE_model
from functions.plot_functions import auxiliar_names, plots
from functions.utils import *

if __name__ == '__main__':

	demograph_parameters, covid_parameters, model_parameters = get_input_data()

	results = run_SEIR_ODE_model(demograph_parameters, covid_parameters, model_parameters)

	filename, legenda = auxiliar_names(covid_parameters, model_parameters)

	results.to_csv(os.path.join(get_output_dir(), filename + '.csv'), index=False)

	plots(filename, legenda, results, demograph_parameters, model_parameters)
