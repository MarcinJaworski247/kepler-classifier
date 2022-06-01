using Microsoft.Extensions.Options;
using WorkerService.Configuration;
using WorkerService.Service;

namespace WorkerService
{
    public class Worker : BackgroundService
    {
        private readonly ILogger<Worker> _logger;
        private string _restApiUrl;
        private string _systemFolderUrl;

        public Worker(ILogger<Worker> logger, IOptions<AppConfiguration> options)
        {
            _logger = logger;
            _restApiUrl = options.Value.RestApiUrl;
            _systemFolderUrl = options.Value.SystemFolderUrl;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            HttpClient client = DataService.InitializeHttpClient();
            DataService.GetData(client, _restApiUrl, _systemFolderUrl);

            while (!stoppingToken.IsCancellationRequested)
            {
                await Task.Delay(TimeSpan.FromHours(24), stoppingToken);
            }
        }
    }
}