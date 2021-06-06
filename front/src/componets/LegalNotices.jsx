import React from "react";
import HeaderMenu from "./HeaderMenu";

const LegalNotices = () => {
    return (
        <div>
        <HeaderMenu/>
        <main className={"termsAndConditions"}>
            <section className={"termsAndConditionsHeader"}>
                <h1>Terms and conditions</h1>
                <p>
                   <b>SurfBetter</b> informs users of the website of its policy of protection of personal data. The use of the
                   <b>SurfBetter</b> web app space and any of the services that are incorporated presupposes
                   the full acceptance of the conditions that are manifested in the privacy policy that is exposed.
                </p>
            </section>
            <section>
                <h2>Data Collect</h2>
                <p>
                    In compliance with Law 15/1999, of December 13, on the protection of personal data, it is reported that
                    the personal data requested in our forms will be included in a personal data file the person in charge
                    and owner of which It’s <b>SurfBetter</b>. Likewise, when a person fills in any of the forms with the personal
                    data requested and accepts the shipment, expressly authorizes <b>SurfBetter</b> to treat or incorporate into
                    the automated file of their property the personal data provided in the aforementioned form and all
                    data that are generated in relation to your participation or use of the different events that are offered
                    on this website.
                </p>
                <p>
                    Unless specifically stated otherwise, it will be considered necessary to fill in all the fields of each
                    form, for which the user must fill out the forms with true, accurate, complete and updated data.
                    The user is solely responsible for any loss or damage, direct or indirect, caused to <b>SurfBetter</b>
                    or any third party by filling out the forms with false, inaccurate, incomplete or outdated
                    information or with data from third parties. Through the different areas that are part of
                    this web space, users can obtain information, make inquiries and participate in the different
                    events that <b>SurfBetter</b> offers through its web space.
                </p>
                <p>
                    As soon as you stop using the <b>SurfBetter</b> application, it deletes all your data regarding the application.
                </p>

            </section>
            <section>
                <h2>Purpose of the treatment</h2>
                <p>
                    The data provided will never be used for a purpose other than that for which they have been assigned,
                    and will be canceled immediately after ceasing to be necessary for this purpose, except when a law
                    establishes otherwise.
                </p>
                <p>
                    The real intention of <b>SurfBetter</b> is to offer a real iteration of the users apart from consulting
                    the data of their favorite beaches. In the form of comments and I like you
                </p>
            </section>
            <section>
                <h2>Security</h2>
                <p>
                    All information regarding personal data received by <b>SurfBetter</b> is treated with the utmost
                    confidentiality,
                    and only the communications strictly necessary for the provision of the service of interest in each
                    case and the communications and assignments authorized by the user through this policy are used. Of privacy.
                </p>
                <p>
                    <b>SurfBetter</b> saves a random token regarding your session when you start the application that is stored
                    locally. This token changes with each login and identifies you as a user throughout the application
                </p>
            </section>
        </main>
        </div>


    )
}
export default LegalNotices