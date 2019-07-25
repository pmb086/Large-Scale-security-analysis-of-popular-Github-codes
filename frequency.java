import java.io.*;
import java.nio.*;
import java.nio.file.*;
import java.util.*;
import org.json.*;

public class frequency {
	
	static HashSet<String> uniqueVuln = new HashSet<String>();
	static ArrayList<String> allVuln = new ArrayList<String>();
	
	static ArrayList<Object> freqCount =  new ArrayList<Object>(); 
	public static int count = 0;
	public static void main(String[] args) throws IOException {
    	BufferedReader readAvailable = new BufferedReader (new FileReader("C:\\Users\\sharmi.Sharmi-PC\\Desktop\\LGTM100\\avail.csv"));
    	String newLine = null;
    	String vulName = null;
    	String temp = null;
    	int total = 0;
    	FileWriter csvFile = new FileWriter("C:\\Users\\sharmi.Sharmi-PC\\Desktop\\LGTM100\\freq.csv");
    	csvFile.append("Vulnerability Name, total occurence");
  	
    	while((newLine=readAvailable.readLine()) != null)
    	{
    		readFile(newLine);
    	}
    	
    	System.out.println(allVuln.size());
    	Iterator<String> frequency = uniqueVuln.iterator();
    	while(frequency.hasNext())
    	{
    		csvFile.append("\n");
    		vulName = frequency.next();
    		total = 0;
    		for(int i =0; i<allVuln.size(); i++)
    		{
    			temp = allVuln.get(i);
    			if(Objects.equals(temp, vulName))
    				total++;
    		}
    		csvFile.append(vulName);
    		csvFile.append(",");
    		csvFile.append(String.valueOf(total));
    	}
    	csvFile.close();
    	
	}

	public static void readFile(String sourceFile) throws UnsupportedEncodingException, IOException
    {
    	String file = "C:\\Users\\sharmi.Sharmi-PC\\Desktop\\LGTM100\\" + sourceFile + ".sarif";
    	String jsonString = new String(Files.readAllBytes(Paths.get(file)), "UTF-8");
        try 
        {
            JSONObject jsonObject = new JSONObject(jsonString);
            @SuppressWarnings("unchecked")
			Iterator<String> keys = jsonObject.keys();
            while(keys.hasNext()) 
            {
                String key = keys.next();
                if(jsonObject.get(key) instanceof JSONArray) 
                {
                    JSONArray array = (JSONArray) jsonObject.get(key);
                    JSONObject object = (JSONObject) array.get(0);
                    @SuppressWarnings("unchecked")
					Iterator<String> innerKeys = object.keys();
                    while(innerKeys.hasNext()) 
                    {
                        String innerKey = innerKeys.next();
                        if(Objects.equals(innerKey, "results"))
                        {
                        	JSONArray resultArray = (JSONArray) object.get(innerKey);
                        	JSONObject resultObject = new JSONObject();
                        	for(int i =0; i<resultArray.length(); i++) 
                        	{
                        		resultObject = resultArray.getJSONObject(i);
                        		@SuppressWarnings("unchecked")
                        		Iterator<String> resultKeys = resultObject.keys();
                        		while(resultKeys.hasNext())
                        		{
                        			String resKey = resultKeys.next();
                            		if(Objects.equals(resKey, "ruleId"))
                            		{
                            			String vul = (String) resultObject.get(resKey);
                            			String vulName[] = vul.split("/");
                            			for (int j=1; j>0; j--)
                            			{
                            				allVuln.add(vulName[2]);
                            			    uniqueVuln.add(vulName[2]);
                            			}
                            		}
                            			
                        		}
                        	}
                        }
                    }
                }
                else
                	continue;
            }
        } catch (JSONException e) 
        {
            e.printStackTrace();
        }
    }

	
}
