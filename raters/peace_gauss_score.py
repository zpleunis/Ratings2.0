import utils
import base
from rating_classes import peace

class PeaceCompositeGaussScoreRater(base.BaseRater):
    short_name = "peace_composite_guass_score"
    long_name = "Composite PEACE Score (Gauss)"
    description = "A composite score using information from all " \
                    "Gaussian-fit-based PEACE ratings. Values are " \
                    "smaller than 0. Usually score > -5 indicates a " \
                    "very good candidate."
                    
    version = 1

    rat_cls = peace.PeaceRatingClass()

    def _compute_rating(self, cand):
        """
        """
        peace = cand.get_from_cache('peace')
        return peace['score_gauss']

Rater = PeaceCompositeGaussScoreRater



