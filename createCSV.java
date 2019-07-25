import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Objects;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class createCSV {

	public static void main(String[] args) throws IOException
	{
		String availFile = null;
		String File = "C:\\Users\\sharmi.Sharmi-PC\\Desktop\\LGTM100\\avail.csv";
		BufferedReader reader = new BufferedReader (new FileReader(File));
		String currentLine = null;
		reader.readLine();
		 Object[] gitArray = null;
		HashSet<String> uniqueVuln = new HashSet<String>();
		FileWriter csvFile = new FileWriter("C:\\Users\\sharmi.Sharmi-PC\\Desktop\\LGTM100\\new.csv");
		csvFile.append("PROJECT NAME, # of Vuln, Vul-1, Vul-2, Vul-3, Vul-4");
		List<String> gitList = new ArrayList<>();
		while((currentLine = reader.readLine())!=null)
    	{
			csvFile.append("\n");
			csvFile.append(currentLine.replace('_', '/'));
			uniqueVuln.clear();
			System.out.println("PROJECT : " +currentLine);
			availFile =  "C:\\Users\\sharmi.Sharmi-PC\\Desktop\\LGTM100\\" + currentLine + ".sarif";
			String jsonString = new String(Files.readAllBytes(Paths.get(availFile)), "UTF-8");
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
	                            			for (int j=1; j>0; j--){
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
			csvFile.append(",");
			csvFile.append(String.valueOf(uniqueVuln.size()));
			Iterator<String> v = uniqueVuln.iterator();
			while(v.hasNext())
			{
				csvFile.append(",");
				csvFile.append(v.next());
			}
			
			csvFile.append((char) uniqueVuln.size());
			csvFile.append(",");
    	}
	csvFile.close();
	}
}
