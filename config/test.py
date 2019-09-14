from config import default
from models import model_tma, model_dta, model_lai, model_glai, model_rvtu, model_rf_ed, model_dt_ed
from over import simple, smote, gan

config = {
    'dataset': {
        'hillstrom': {
            'tma': {},
            'tma_simple': {'over_sampling': simple.over_sampling},
            # 'tma_smote': {'over_sampling': smote.over_sampling},
            # 'tma_gan': {'over_sampling': gan.over_sampling},
        },
    },
    'wrapper': False,
    'niv': False,
    'tune': False,
}
