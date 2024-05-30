# Frappe Better List View © 2024
# Author:  Ameen Ahmed
# Company: Level Up Marketing & Software Development Services
# Licence: Please refer to LICENSE file


from frappe import __version__


# [Internal]
__frappe_version__ = int(__version__.split(".")[0])


# [Hooks]
def is_version_gt(num: int):
    return __frappe_version__ > num