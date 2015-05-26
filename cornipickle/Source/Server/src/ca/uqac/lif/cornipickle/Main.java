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

import java.io.PrintStream;
import java.util.List;

import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.OptionBuilder;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.PosixParser;

import ca.uqac.lif.cornipickle.util.AnsiPrinter;

public class Main
{  
  /**
   * Return codes
   */
  public static final int ERR_OK = 0;
  public static final int ERR_PARSE = 2;
  public static final int ERR_IO = 3;
  public static final int ERR_ARGUMENTS = 4;
  public static final int ERR_RUNTIME = 6;
  public static final int ERR_GRAMMAR = 7;
  public static final int ERR_INPUT = 9;

  /**
   * Build string to identify versions
   */
  protected static final String VERSION_STRING = "0.0";
  protected static final String BUILD_STRING = "20150126";
  
  /**
   * Verbosity level for CLI
   */
  protected static int s_verbosity = 1;
  
  /**
   * Main method
   * @param args Command-line arguments
   */
  public static void main(String[] args)
  {
    final AnsiPrinter stderr = new AnsiPrinter(System.err);
    final AnsiPrinter stdout = new AnsiPrinter(System.out);
    stdout.setForegroundColor(AnsiPrinter.Color.BLACK);
    stderr.setForegroundColor(AnsiPrinter.Color.BLACK);
    
    // Propertly close print streams when closing the program
    // https://www.securecoding.cert.org/confluence/display/java/FIO14-J.+Perform+proper+cleanup+at+program+termination
    Runtime.getRuntime().addShutdownHook(new Thread(new Runnable()
    {
      @Override
      public void run()
      {
        stderr.close();
        stdout.close();
      }
    }));

    // Parse command line arguments
    Options options = setupOptions();
    CommandLine c_line = setupCommandLine(args, options, stderr);
    assert c_line != null;
    if (c_line.hasOption("verbosity"))
    {
      s_verbosity = Integer.parseInt(c_line.getOptionValue("verbosity"));
    }
    if (s_verbosity > 0)
    {
      showHeader(stdout);
    }
    if (c_line.hasOption("version"))
    {
      stderr.println("(C) 2015 Sylvain Hallé et al., Université du Québec à Chicoutimi");
      stderr.println("This program comes with ABSOLUTELY NO WARRANTY.");
      stderr.println("This is a free software, and you are welcome to redistribute it");
      stderr.println("under certain conditions. See the file LICENSE for details.\n");
      System.exit(ERR_OK);
    }
    if (c_line.hasOption("h"))
    {
      showUsage(options);
      System.exit(ERR_OK);
    }
    Pipe namedPipe = new Pipe();
    namedPipe.read();
    /* 
      DO STUFF WITH THE STUFF
    */
    namedPipe.write();
  }
  
  protected static void println(PrintStream out, String message, int verbosity_level)
  {
    if (verbosity_level >= s_verbosity)
    {
      out.println(message);
    }
  }

  /**
   * Sets up the options for the command line parser
   * @return The options
   */
  @SuppressWarnings("static-access")
  private static Options setupOptions()
  {
    Options options = new Options();
    Option opt;
    opt = OptionBuilder
        .withLongOpt("help")
        .withDescription(
            "Display command line usage")
            .create("h");
    options.addOption(opt);
    return options;
  }
  
  /**
   * Show the benchmark's usage
   * @param options The options created for the command line parser
   */
  private static void showUsage(Options options)
  {
    HelpFormatter hf = new HelpFormatter();
    hf.printHelp("java -jar Cornipickle.jar [options] [file1 [file2 ...]]", options);
  }
  /**
   * Sets up the command line parser
   * @param args The command line arguments passed to the class' {@link main}
   * method
   * @param options The command line options to be used by the parser
   * @return The object that parsed the command line parameters
   */
  private static CommandLine setupCommandLine(String[] args, Options options, PrintStream stderr)
  {
    CommandLineParser parser = new PosixParser();
    CommandLine c_line = null;
    try
    {
      // parse the command line arguments
      c_line = parser.parse(options, args);
    }
    catch (org.apache.commons.cli.ParseException exp)
    {
      // oops, something went wrong
      stderr.println("ERROR: " + exp.getMessage() + "\n");
      //HelpFormatter hf = new HelpFormatter();
      //hf.printHelp(t_gen.getAppName() + " [options]", options);
      System.exit(ERR_ARGUMENTS);
    }
    return c_line;
  }
  
  private static void showHeader(PrintStream out)
  {
    out.println("Cornipickle, a web oracle");
    out.println("Version " + VERSION_STRING + ", build " + BUILD_STRING);
  }
  

}