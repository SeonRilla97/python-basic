from locust import HttpUser, task, between

BODY = """<?xml version="1.0" encoding="UTF-8"?>
<Root xmlns="http://www.nexacroplatform.com/platform/dataset">
    <Parameters>
        <Parameter id="apt.uid">AP-YFGMCGUNNIFB-2-1767061094128-77565268.0.2.6b933aba-006b-4c12-b4b5-a0ddc2adfcf4</Parameter>
        <Parameter id="_ga">GA1.1.504938686.1767061095</Parameter>
        <Parameter id="_ga_0C4M1PWYZ7">GS2.1.s1775611631$o48$g1$t1775612361$j60$l0$h0</Parameter>
        <Parameter id="_ga_T11SF3WXX2">GS2.1.s1775611631$o48$g1$t1775612361$j60$l0$h0</Parameter>
        <Parameter id="_ga_K2SPJK2C73">GS2.1.s1775611631$o48$g1$t1775612361$j60$l0$h0</Parameter>
    </Parameters>
    <Dataset id="dsRequestSearch">
        <ColumnInfo>
            <Column id="startDate" type="STRING" size="100" />
            <Column id="endDate" type="STRING" size="100" />
            <Column id="requestCategory" type="STRING" size="100" />
            <Column id="requestType" type="STRING" size="100" />
            <Column id="customerId" type="STRING" size="100" />
            <Column id="customerName" type="STRING" size="100" />
            <Column id="requestTitle" type="STRING" size="100" />
            <Column id="requestContent" type="STRING" size="100" />
        </ColumnInfo>
        <Rows>
            <Row>
            </Row>
        </Rows>
    </Dataset>
    <Dataset id="_BackendServiceInfo">
        <ColumnInfo>
            <Column id="name" type="STRING" size="256" />
            <Column id="project" type="STRING" size="256" />
        </ColumnInfo>
        <Rows>
            <Row>
                <Col id="name">model/svcRequest</Col>
                <Col id="project" />
            </Row>
        </Rows>
    </Dataset>
</Root>"""

HEADERS = {
    "accept": "application/xml, text/xml, */*",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache, no-store",
    "content-type": "text/xml",
    "expires": "-1",
    "if-modified-since": "Sat, 01 Jan 2000 00:00:00 GMT",
    "origin": "https://dev-apps.dev.neopangea.link",
    "pragma": "no-cache",
    "referer": "https://dev-apps.dev.neopangea.link/space-o5y4jle/project-8dpoi1o/app-82vexgf/deploy-zt8pg2vkmhnqsm/",
    "x-requested-with": "Fetch",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    "cookie": "apt.uid=AP-YFGMCGUNNIFB-2-1767061094128-77565268.0.2.6b933aba-006b-4c12-b4b5-a0ddc2adfcf4; _ga=GA1.1.504938686.1767061095; _ga_0C4M1PWYZ7=GS2.1.s1775611631$o48$g1$t1775612361$j60$l0$h0; _ga_T11SF3WXX2=GS2.1.s1775611631$o48$g1$t1775612361$j60$l0$h0; _ga_K2SPJK2C73=GS2.1.s1775611631$o48$g1$t1775612361$j60$l0$h0",
}

class NexacroUser(HttpUser):
    host = "https://dev-apps.dev.neopangea.link"
    wait_time = between(1, 3)

    @task
    def execute(self):
        self.client.post(
            "/space-o5y4jle/project-8dpoi1o/app-82vexgf/deploy-zt8pg2vkmhnqsm/api/v1/execute",
            data=BODY.encode("utf-8"),
            headers=HEADERS,
        )

    @task
    def execute(self):
        with self.client.post(
            "/space-o5y4jle/project-8dpoi1o/app-82vexgf/deploy-zt8pg2vkmhnqsm/api/v1/execute",
            data=BODY.encode("utf-8"),
            headers=HEADERS,
            catch_response=True
        ) as response:
            print(f"status: {response.status_code}")
            print(f"body: {response.text[:500]}")  # 앞 500자만        