from textwrap import dedent
from crewai import Task

class AnalysisPreparationTasks():
    def product_analysis_task(self, agent, product_description):
    return Task(
        description=dedent(f"""
        Analyze the provided product information and provide insights on the product's condition, market trends, and price fairness.
        Product Description: {product_description}
        """),
        expected_output=dedent("""
        A detailed report containing product analysis insights, including the product's condition, market trends, and an assessment of the price fairness.
        """),
        async_execution=True,
        agent=agent
    )

    def review_analysis_task(self, agent, product_description):
        return Task(
            description=dedent(f"""
            Collect and analyze customer reviews and expert opinions related to the product. Provide insights into the product's quality, performance, and overall customer satisfaction.
            Product Description: {product_description}
            """),
            expected_output=dedent("""
            A report summarizing the insights derived from the analysis of customer reviews and expert opinions, focusing on product quality, performance, and customer satisfaction.
            """),
            async_execution=True,
            agent=agent
        )

    def fraud_assessment_task(self, agent, product_description, price):
        return Task(
            description=dedent(f"""
            Assess potential fraud risks associated with the purchasing channel based on the product information and price. Provide a fraud risk assessment and recommend mitigation measures.
            Product Description: {product_description}
            Price: {price}
            """),
            expected_output=dedent("""
            A comprehensive fraud risk assessment that identifies potential fraud risks associated with the purchasing channel and provides recommendations for risk mitigation.
            """),
            agent=agent
        )

    def final_report_task(self, agent, product_description, price):
        return Task(
            description=dedent(f"""
            Review and consolidate the findings from the product analysis, review analysis, and fraud assessment. Prepare a final report that provides an overall assessment of the product, its price fairness, and any potential risks or concerns.
            Product Description: {product_description}
            Price: {price}
            """),
            expected_output=dedent("""
            A comprehensive final report that includes product analysis, review insights, fraud risk assessment, and an overall recommendation regarding the product and its price.
            """),
            agent=agent
        )