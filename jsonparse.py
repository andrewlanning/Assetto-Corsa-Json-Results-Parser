import jsonscraper

server_results_path = "E:\\SteamLibrary\\steamapps\\common\\assettocorsa\\server\\results"

result_files = jsonscraper.get_results_files(server_results_path)
jsonscraper.scrape_results(result_files)