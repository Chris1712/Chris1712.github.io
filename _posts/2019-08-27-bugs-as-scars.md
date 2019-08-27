---
layout: post
title:  "Bugs that leave scars"
author: Chris
tags: engineering
---

My team has been working on an issue where our product would, under some circumstances, write duplicate rows into one of our database tables. Since the table had no uniqueness constraints the writes succeeded, but later reads of those duplicate rows would cause the product to crash, and it was this crash we were investigating.

Once we realised the problem and fixed our product to no longer insert duplicates, we were faced with a problem: the duplicate data in customer databases could still exist, and since deployments are controlled by our customers, we had no way to directly intervene.

So, two options presented themselves: we could modify our software further, to handle reads of duplicate rows, or we could take the fairly onerous responsibility of developing scripts to clear out the bad data safely, and ideally without any manual intervention from our support team.

In many ways the first option is preferable: it's quicker and safer, and we don't have to run the risk of trying to meddle with customer databases. But I think the second choice is the correct one.

It was my gut instinct to avoid adding extra code just to cope with the aftermath of a previous bug; it feels like *scar tissue* left in the product forever, adding no value and weighing everything down unnecessarily. Our product is a long-lived one, and every line of code has a maintenance cost that we'll be paying for years to come.

There are other problems too: the functionality where our bug cropped up didn't cope with duplicate data, but really, the entire product was built with the assumption of uniqueness in that data; how could we be confident there were no other circumstances where leaving these duplicates might cause further bugs?

Not only that, but the prolonged possibility of the bad data existing in databases we needed to interact would mean us having to factor that into future design decisions, too, to ensure any other components that used the data could also cope with duplication.

In the end we took the path of fixing the data, and I'm glad we were able to do that, to fix that bug without leaving any scarring in the product. But the experience has left me wondering if there are any other places in our product where scars have been left behind...