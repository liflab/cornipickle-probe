/*
    Cornipickle, validation of layout bugs in web applications
    Copyright (C) 2015 Sylvain Hallé

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
package ca.uqac.lif.cornipickle;

import ca.uqac.lif.json.JsonElement;

public class ExistsStatement extends Quantifier
{
  public ExistsStatement()
  {
    super();
    m_startValue = Verdict.Value.FALSE;
    m_cutoffValue = Verdict.Value.TRUE;
  }
  
  @Override
  protected Verdict evaluationFunction(Verdict x, Verdict y, JsonElement e)
  {
    x.disjoin(y, e);
    return x;
  }
  
  @Override
  public String toString(String indent)
  {
    StringBuilder out = new StringBuilder();
    out.append(indent).append("There exists a ").append(m_variable).append(" in ").append(m_set).append(" such that\n");
    out.append(m_innerStatement.toString(indent + "  "));
    return out.toString();
  }
  
  @Override
  public ExistsStatement getClone()
  {
    ExistsStatement out = new ExistsStatement();
    out.m_innerStatement = m_innerStatement.getClone();
    out.m_variable = m_variable;
    out.m_set = m_set.getClone();
    return out;
  }
}
