"""configuration class class_config.py"""
pars_ = {}

def get_parameter(par_):
    """Get config parameter"""
    return pars_[par_]

class Config:
    """class to obtain config parameters"""
    def get_par(self, par__):
        """Get config parameter"""
        return get_parameter(par__)
    def set_par(self, par__, val__):
        """Set config parameter"""
        pars_[par__]=val__

#parametros de paths

pars_["src_dir"]="C:/RSILVA_BASIC_BOTS/TEST_IMAGENES_caticatura/"
pars_["out_dir"]="C:/RSILVA_BASIC_BOTS/TEST_IMAGENES_caticatura/out/"
pars_["car_dir"]="C:/RSILVA_BASIC_BOTS/TEST_IMAGENES_caticatura/car/"

#parametros de debug
pars_['debug_mode' ]=True#yes/no
pars_['generar_frame']=True#
