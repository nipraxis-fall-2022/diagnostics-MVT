""" Scan outlier metrics
"""

# Any imports you need
import numpy as np


def dvars(img):
    """ Calculate dvars metric on Nibabel image `img`

    The dvars calculation between two volumes is defined as the square root of
    (the mean of the (voxel differences squared)).

    Parameters
    ----------
    img : nibabel image

    Returns
    -------
    dvals : 1D array
        One-dimensional array with n-1 elements, where n is the number of
        volumes in `img`.
    """

    #get data
    data = img.get_fdata()

    #calculate
    n_voxels = np.prod(data.shape[:-1])
    n_vols = data.shape[-1]
    data_array = data.reshape(n_voxels, n_vols)

    vol_diff = np.diff(data_array, axis = 1)
    dvals = np.sqrt(np.mean(vol_diff**2, axis = 0))

    return(dvals)




    # Hint: remember 'axis='.  For example:
    # In [2]: arr = np.array([[2, 3, 4], [5, 6, 7]])
    # In [3]: np.mean(arr, axis=1)
    # Out[2]: array([3., 6.])
    #
    # You may be be able to solve this in four lines, without a loop.
    # But solve it any way you can.
    # This is a placeholder, replace it to write your solution.
    #raise NotImplementedError('Code up this function')
