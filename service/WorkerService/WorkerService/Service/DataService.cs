using System.Net.Http.Json;
using WorkerService.Model;
using CsvHelper;
using System.Globalization;

namespace WorkerService.Service
{
    public class DataService
    {
        public static HttpClient InitializeHttpClient()
        {
            HttpClient client = new HttpClient();
            return client;
        }
        public static async void GetData(HttpClient client)
        {
            //TODO: move URI to appsettings.json
            const string URI = @"https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&format=json";
            List<Data> data = new List<Data>();

            try
            {
                data = await client.GetFromJsonAsync<List<Data>>(URI);
            } catch(Exception ex)
            {
                Console.WriteLine(ex);
            }

            SaveToCSV(data);
        }
        internal static void SaveToCSV(List<Data> data)
        {
            //TODO: move csv path to appsettings.json
            string csvPath = @"D:\keppler-classifier\keppler-data.csv";
            if (data.Count > 0)
            {
                using (var streamWriter = new StreamWriter(csvPath))
                {
                    //TODO: file operations permissions checking
                    using (var csvWriter = new CsvWriter(streamWriter, CultureInfo.InvariantCulture))
                    {
                        csvWriter.WriteRecords(data);
                    }
                }

            }
        }
    }
}
