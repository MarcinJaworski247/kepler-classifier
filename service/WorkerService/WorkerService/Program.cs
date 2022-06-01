using WorkerService;
using WorkerService.Configuration;

IHost host = Host.CreateDefaultBuilder(args)
    .UseWindowsService(options =>
    {
        options.ServiceName = "Kepler Classifier service";
    })
    .ConfigureServices((hostContext, services) =>
    {
        IConfiguration configuration = hostContext.Configuration;
        services.Configure<AppConfiguration>(configuration.GetSection(nameof(AppConfiguration)));
        services.AddHostedService<Worker>();
    })
    .Build();

await host.RunAsync();
