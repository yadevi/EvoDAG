# Copyright 2016 Mario Graff Guerrero

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from test_root import X, cl


def test_generational_generation():
    from EvoDAG.population import Generational
    from EvoDAG import EvoDAG
    gp = EvoDAG(population_class='Generational',
                popsize=10)
    gp.X = X
    y = cl.copy()
    y[y != 1] = -1
    gp.y = y
    gp.create_population()
    assert isinstance(gp.population, Generational)
    p = []
    for i in range(gp.popsize-1):
        a = gp.random_offspring()
        p.append(a)
        gp.replace(a)
    assert len(gp.population._inner) == (gp.popsize - 1)
    a = gp.random_offspring()
    p.append(a)
    gp.replace(a)
    assert len(gp.population._inner) == 0
    for a, b in zip(gp.population.population, p):
        assert a == b