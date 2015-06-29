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

import ca.uqac.lif.cornipickle.json.JsonNumber;

public abstract class Operation extends Property
{
  protected NumberConstant m_left;
  protected NumberConstant m_right;
  
  public Operation(NumberConstant n1, NumberConstant n2) 
  {
    super();
    setLeft(n1);
    setRight(n2);
  }

  public Operation(JsonNumber n1, JsonNumber n2) 
  {
    super();
    setLeft(new NumberConstant(n1));
    setRight(new NumberConstant(n2));
  }
  
  public void setLeft(NumberConstant p)
  {
    m_left = p;
  }
  
  public void setRight(NumberConstant p)
  {
    m_right = p;
  }

  @Override
  public final void postfixAccept(LanguageElementVisitor visitor)
  {
    m_left.postfixAccept(visitor);
    m_right.postfixAccept(visitor);
    visitor.visit(this);
    visitor.pop();
  }
  
  @Override
  public final void prefixAccept(LanguageElementVisitor visitor)
  {
    visitor.visit(this);
    m_left.prefixAccept(visitor);
    m_right.prefixAccept(visitor);
    visitor.pop();
  }

}
