# Copyright 2020 MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import numpy as np
from parameterized import parameterized

from monai.transforms import RandGaussianSmoothd

TEST_CASE_1 = [
    {"keys": "img", "sigma_x": (0.5, 1.5), "prob": 1.0},
    {"img": np.array([[[1, 1, 1], [2, 2, 2], [3, 3, 3]], [[4, 4, 4], [5, 5, 5], [6, 6, 6]]])},
    np.array(
        [
            [[0.71806467, 0.9074683, 0.71806467], [1.0718315, 1.3545481, 1.0718315], [1.0337002, 1.306359, 1.0337002]],
            [[2.0318885, 2.5678391, 2.0318885], [2.6795788, 3.3863702, 2.6795788], [2.3475242, 2.9667296, 2.3475242]],
        ]
    ),
]

TEST_CASE_2 = [
    {"keys": "img", "sigma_x": (0.5, 1.5), "sigma_y": (0.5, 1.0), "prob": 1.0},
    {"img": np.array([[[1, 1, 1], [2, 2, 2], [3, 3, 3]], [[4, 4, 4], [5, 5, 5], [6, 6, 6]]])},
    np.array(
        [
            [[0.7686928, 0.9848021, 0.7686928], [1.1474025, 1.4699818, 1.1474024], [1.1065826, 1.4176859, 1.1065826]],
            [[2.1751494, 2.7866683, 2.1751497], [2.8685062, 3.6749542, 2.8685062], [2.5130394, 3.219552, 2.5130394]],
        ]
    ),
]


class TestRandGaussianSmoothd(unittest.TestCase):
    @parameterized.expand([TEST_CASE_1, TEST_CASE_2])
    def test_value(self, argments, image, expected_data):
        converter = RandGaussianSmoothd(**argments)
        converter.set_random_state(seed=0)
        result = converter(image)
        np.testing.assert_allclose(result["img"], expected_data, rtol=1e-4)


if __name__ == "__main__":
    unittest.main()
