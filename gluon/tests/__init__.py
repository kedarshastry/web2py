import sys

from .test_http import *
from .test_contenttype import *
from .test_fileutils import *
from .test_globals import *
from .test_recfile import *
from .test_storage import *
from .test_dal import *
from .test_cache import *
from .test_template import *
from .test_html import *
from .test_contribs import *
from .test_routes import *
from .test_router import *
from .test_validators import *
from .test_tools import *
from .test_utils import *
from .test_serializers import *
from .test_languages import *
from .test_compileapp import *
from .test_appadmin import *
from .test_web import *

if sys.version[:3] == '2.7':
    from .test_is_url import *
    from .test_scheduler import *
    from .test_old_doctests import *
