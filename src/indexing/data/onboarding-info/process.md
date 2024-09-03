## New Onboarding Process

- Before starting the onboarding process, please read through all the steps below and ensure you have the following information:
    - Name and email address of the current account DPE, BGB ID, BAC ID, BAM ID, GSMA code, CHIP ID, and CDIR - all which can be identified in BlueID.
    - The country or market the account belongs to.
    - Your account will need to be CBC compliant, which means the account accepts the hosting location and the support locations for your hosting location. You can check the current hosting locations and support locations in the Security Whitepaper.
    - Know what tools are used for IPC and Event Management. You are required to know the URLs for your source endpoints individually for Incidents, Problems and Change; the User Credentials for these; and the inventory tool your account uses.
    - A list of contacts: Account Admin, an account UAT Tester, and an account BYOD admin.
- Once you have all required information in section 1, your next step is to fill in the “Request Onboarding to Integrated AIOPS” in ServiceNow. If you need help knowing how to fill in a Service Request, please review these instructions.
- IMPORTANT: In the service request there will be a link to an MS Form. The form requires the Service Request Number you just filled as required in section 2. This form will ask for the information detailed in section 1 of this list plus other details. 
- Once the SR and the MS Forms are submitted these tasks will happen in the background:
    - The Onboarding Transition Team will confirm all the information in the form was properly filled. If it isn't, they'll reach out to the contacts provided in the MS form.
    - The Integrated AIOps Delivery team will create the account OU.
    - The Transition team will verify the account is CBC compliant.
    - The Delivery team will Configure CTM for the account.
    - The Delivery team will enable the Common Catalogue for the account.
    - The extensions team will configure the IPC and Event Management extensions.
    - In case there isn't an available extension yet for the account's IPC or Event Managment tools, the delivery team will enable BYOD access to the account.
T   - ransition and Delivery teams will validate if account has reached status of Boarded as per the definition in the Onboarding States Presentation listed further down in this page.
    - Once the account reaches Boarded status, the Delivery team will give account admin access in ARMS to the Account DPE, which gives him the rights to approve other users requesting access to the account.
    - The Transition team will hand over the account to BAU.