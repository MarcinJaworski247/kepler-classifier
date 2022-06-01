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
        public static async void GetData(HttpClient client, string restApiUrl, string systemFolderUrl)
        {
            List<Data> data = new List<Data>();

            try
            {
                data = await client.GetFromJsonAsync<List<Data>>(restApiUrl);
            } catch(Exception ex)
            {
                Console.WriteLine(ex);
            }

            SaveToCSV(data, systemFolderUrl);
        }
        internal static void SaveToCSV(List<Data> data, string systemFolderUrl)
        {
            string csvPath = systemFolderUrl;
            if (data.Count > 0)
            {
                using var streamWriter = new StreamWriter(csvPath);
                using var csvWriter = new CsvWriter(streamWriter, CultureInfo.InvariantCulture);
                csvWriter.WriteRecords(data);

            }
        }
    }
}
