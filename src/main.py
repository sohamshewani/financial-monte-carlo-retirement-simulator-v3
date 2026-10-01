from src import portfolio, monte_carlo, tax_loss_harvesting, reporting

if __name__ == '__main__':
    # Example usage
    investments = portfolio.load_investments('data/sample_investments.csv')
    portfolios = portfolio.load_portfolios('data/sample_portfolios.csv')
    report_data = reporting.generate_report()

    # Monte Carlo simulation
    simulation_results = monte_carlo.run_simulation(investments, portfolios, report_data)
    print(simulation_results)

    # Tax loss harvesting
    harvesting_results = tax_loss_harvesting.apply_harvesting(investments)
    print(harvesting_results)