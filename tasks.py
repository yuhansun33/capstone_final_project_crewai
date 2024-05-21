from textwrap import dedent
from crewai import Task

class AnalysisPreparationTasks():
    def project_initiation_task(self, agent, project_scope, customer_requirements):
        return Task(
            description=dedent(f"""
            Initiate the analysis project by reviewing the project scope and customer
            requirements. Develop a project plan that includes timelines, analysis
            requirements, and task assignments.

            Project Scope: {project_scope}
            Customer Requirements: {customer_requirements}"""),
            expected_output=dedent("""
            A comprehensive project plan that outlines the project timeline, analysis
            requirements, and task assignments for each team member."""),
            async_execution=True,
            agent=agent
        )

    def product_data_analysis_task(self, agent, project_scope):
        return Task(
            description=dedent(f"""
            Collect and analyze product data from various sources within the scope of
            the project. Provide structured and processed product data insights that
            will contribute to the overall analysis.

            Project Scope: {project_scope}"""),
            expected_output=dedent("""
            A detailed report containing structured and processed product data insights
            that can be used for further analysis and decision-making."""),
            async_execution=True,
            agent=agent
        )

    def customer_feedback_analysis_task(self, agent, project_scope):
        return Task(
            description=dedent(f"""
            Collect and analyze customer reviews, feedback, and expert opinions related
            to the project scope. Provide insights and recommendations based on the
            analysis of customer sentiment and feedback.

            Project Scope: {project_scope}"""),
            expected_output=dedent("""
            A report summarizing the insights and recommendations derived from the
            analysis of customer feedback and expert opinions."""),
            async_execution=True,
            agent=agent
        )

    def risk_assessment_task(self, agent, project_scope):
        return Task(
            description=dedent(f"""
            Assess potential risks and fraudulent activities based on the product data
            and customer feedback analysis within the project scope. Provide a risk
            evaluation report highlighting areas of concern and recommend mitigation
            strategies.

            Project Scope: {project_scope}"""),
            expected_output=dedent("""
            A comprehensive risk evaluation report that identifies potential risks,
            highlights areas of concern, and provides recommendations for risk
            mitigation."""),
            agent=agent
        )

    def final_analysis_report_task(self, agent, project_scope, customer_requirements):
        return Task(
            description=dedent(f"""
            Review and consolidate the findings from the product data analysis, customer
            feedback analysis, and risk assessment. Prepare a final analysis report that
            meets the project scope and customer requirements.

            Project Scope: {project_scope}
            Customer Requirements: {customer_requirements}"""),
            expected_output=dedent("""
            A comprehensive final analysis report that includes product evaluations,
            pricing insights, risk assessments, and recommendations based on the
            consolidated findings."""),
            agent=agent
        )