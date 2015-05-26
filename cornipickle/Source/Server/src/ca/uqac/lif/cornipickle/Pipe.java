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

import java.io.*;
import java.lang.StringBuilder;

public class Pipe
{
    protected BufferedReader reader;
    protected StringBuilder buffer;

    public Pipe()
    {
        super();
        reader = new BufferedReader(new InputStreamReader(System.in));
        buffer = new StringBuilder();
    }

    public void read()
    {
        try
        {
            String s = reader.readLine();
            while(s.equals("x")==false)
            {
                buffer.append(s);
                s = reader.readLine();
            }
            PrintWriter writer = new PrintWriter("resultJava.txt", "UTF-8");
            writer.println(buffer);
            writer.close();
        }
        catch(IOException e)
        {
            e.printStackTrace();
        }
    }

    public void write()
    {
        System.out.println("First msg from java");
        System.out.println("Second msg from java");
        System.out.println("x");
    }
}