
#####Load data set#####
fisheries <- readXL("F:/SOIS-project/Fisheries project/survey - USSD among FIsher women - final.xlsx", rownames=FALSE, header=TRUE, na="", sheet="Main Sheet", 
  stringsAsFactors=TRUE)
library(tcltk, pos=15)
#####Numerical summaries#####
res <- NULL
res <- numSummary(fisheries[,"age"], groups=fisheries$Willingness.to.use.Mobile.Banking, statistics=c("mean", "sd", "quantiles"), quantiles=c(0,.25,.5,.75,1))
colnames(res$table)[1:2] <- gettextRcmdr( colnames(res$table)[1:2])
res
#####Two-sample t-test#####
group.names <- NULL
group.means <- NULL
group.sds <- NULL
group.p <- NULL
res <- NULL
(res <- t.test(age~factor(Willingness.to.use.Mobile.Banking), alternative='two.sided', conf.level=0.95, var.equal=TRUE, data=fisheries))
windows(width=7, height=7); par(lwd=1, las=1, family="sans", cex=1, mgp=c(3.0,1,0))
bar.means <- tapply(fisheries$age, factor(fisheries$Willingness.to.use.Mobile.Banking), mean, na.rm=TRUE)
bar.sds <- tapply(fisheries$age, factor(fisheries$Willingness.to.use.Mobile.Banking), sd, na.rm=TRUE)
bar.sds <- ifelse(is.na(bar.sds), 0, bar.sds)
barx <- barplot(bar.means, ylim=c(ifelse(min(bar.means, na.rm=TRUE)>0, 0, min(bar.means-bar.sds, na.rm=TRUE)*1.2), max(bar.means+bar.sds, na.rm=TRUE)*1.2), 
  xlab="Willingness.to.use.Mobile.Banking", ylab="age", axis.lty=1)
error.bar(barx, bar.means, bar.sds)
group.names <- c(group.names, "Willingness.to.use.Mobile.Banking=0")
group.means <- c(group.means, bar.means[1])
group.sds <- c(group.sds, bar.sds[1])
group.p <- c(group.p, signif(res$p.value,digits=3))
group.names <- c(group.names, "Willingness.to.use.Mobile.Banking=1")
group.means <- c(group.means, bar.means[2])
group.sds <- c(group.sds, bar.sds[2])
group.p <- c(group.p, "")
summary.ttest <- NULL
summary.ttest <- data.frame(mean=group.means, sd=group.sds, p.value=group.p)
rownames(summary.ttest) <- group.names
colnames(summary.ttest) <- gettextRcmdr(colnames(summary.ttest))
summary.ttest
#####Numerical summaries#####
res <- NULL
res <- numSummary(fisheries[,"age"], groups=fisheries$Traning.for.Mobile.Banking, statistics=c("mean", "sd", "quantiles"), quantiles=c(0,.25,.5,.75,1))
colnames(res$table)[1:2] <- gettextRcmdr( colnames(res$table)[1:2])
res
#####Two-sample t-test#####
group.names <- NULL
group.means <- NULL
group.sds <- NULL
group.p <- NULL
res <- NULL
(res <- t.test(age~factor(Traning.for.Mobile.Banking), alternative='two.sided', conf.level=0.95, var.equal=TRUE, data=fisheries))
windows(width=7, height=7); par(lwd=1, las=1, family="sans", cex=1, mgp=c(3.0,1,0))
bar.means <- tapply(fisheries$age, factor(fisheries$Traning.for.Mobile.Banking), mean, na.rm=TRUE)
bar.sds <- tapply(fisheries$age, factor(fisheries$Traning.for.Mobile.Banking), sd, na.rm=TRUE)
bar.sds <- ifelse(is.na(bar.sds), 0, bar.sds)
barx <- barplot(bar.means, ylim=c(ifelse(min(bar.means, na.rm=TRUE)>0, 0, min(bar.means-bar.sds, na.rm=TRUE)*1.2), max(bar.means+bar.sds, na.rm=TRUE)*1.2), 
  xlab="Traning.for.Mobile.Banking", ylab="age", axis.lty=1)
error.bar(barx, bar.means, bar.sds)
group.names <- c(group.names, "Traning.for.Mobile.Banking=0")
group.means <- c(group.means, bar.means[1])
group.sds <- c(group.sds, bar.sds[1])
group.p <- c(group.p, signif(res$p.value,digits=3))
group.names <- c(group.names, "Traning.for.Mobile.Banking=1")
group.means <- c(group.means, bar.means[2])
group.sds <- c(group.sds, bar.sds[2])
group.p <- c(group.p, "")
summary.ttest <- NULL
summary.ttest <- data.frame(mean=group.means, sd=group.sds, p.value=group.p)
rownames(summary.ttest) <- group.names
colnames(summary.ttest) <- gettextRcmdr(colnames(summary.ttest))
summary.ttest
#####Numerical summaries#####
res <- NULL
res <- numSummary(fisheries[,"Education"], groups=fisheries$Willingness.to.use.Mobile.Banking, statistics=c("mean", "sd", "quantiles"), quantiles=c(0,.25,.5,
  .75,1))
colnames(res$table)[1:2] <- gettextRcmdr( colnames(res$table)[1:2])
res
#####Mann-Whitney U test#####
group.names <- NULL
group.median <- NULL
group.min <- NULL
group.max <- NULL
group.1Q <- NULL
group.3Q <- NULL
group.p <- NULL
windows(width=7, height=7); par(lwd=1, las=1, family="sans", cex=1, mgp=c(3.0,1,0))
boxplot(Education~ factor(Willingness.to.use.Mobile.Banking), ylab="Education", xlab="Willingness.to.use.Mobile.Banking", data=fisheries)
(res <- wilcox.test(Education ~ factor(Willingness.to.use.Mobile.Banking), alternative="two.sided", data=fisheries))
group.names <- c(group.names, "Willingness.to.use.Mobile.Banking=0")
group.min <- c(group.min, with(fisheries, min(Education[Willingness.to.use.Mobile.Banking=='0'], na.rm=TRUE)))
group.1Q <- c(group.1Q, with(fisheries, quantile(Education[Willingness.to.use.Mobile.Banking=='0'], 0.25, na.rm=TRUE)))
group.median <- c(group.median, with(fisheries, median(Education[Willingness.to.use.Mobile.Banking=='0'], na.rm=TRUE)))
group.3Q <- c(group.3Q, with(fisheries, quantile(Education[Willingness.to.use.Mobile.Banking=='0'], 0.75, na.rm=TRUE)))
group.max <- c(group.max, with(fisheries, max(Education[Willingness.to.use.Mobile.Banking=='0'], na.rm=TRUE)))
group.p <- c(group.p, signif(res$p.value,digits=3))
group.names <- c(group.names, "Willingness.to.use.Mobile.Banking=1")
group.min <- c(group.min, with(fisheries, min(Education[Willingness.to.use.Mobile.Banking=='1'], na.rm=TRUE)))
group.1Q <- c(group.1Q, with(fisheries, quantile(Education[Willingness.to.use.Mobile.Banking=='1'], 0.25, na.rm=TRUE)))
group.median <- c(group.median, with(fisheries, median(Education[Willingness.to.use.Mobile.Banking=='1'], na.rm=TRUE)))
group.3Q <- c(group.3Q, with(fisheries, quantile(Education[Willingness.to.use.Mobile.Banking=='1'], 0.75, na.rm=TRUE)))
group.max <- c(group.max, with(fisheries, max(Education[Willingness.to.use.Mobile.Banking=='1'], na.rm=TRUE)))
group.p <- c(group.p, "")
mannwhitney.table <- NULL
mannwhitney.table <- data.frame(Minimum=group.min, Q1=group.1Q, Median=group.median, Q3=group.3Q, Maximum=group.max, p.value=group.p)
rownames(mannwhitney.table) <- group.names
colnames(mannwhitney.table)[c(2,4)] <- c("25%", "75%")
colnames(mannwhitney.table) <- gettextRcmdr(colnames(mannwhitney.table))
mannwhitney.table
#####Mann-Whitney U test#####
group.names <- NULL
group.median <- NULL
group.min <- NULL
group.max <- NULL
group.1Q <- NULL
group.3Q <- NULL
group.p <- NULL
windows(width=7, height=7); par(lwd=1, las=1, family="sans", cex=1, mgp=c(3.0,1,0))
boxplot(Education~ factor(Willingness.to.use.Mobile.Banking), ylab="Education", xlab="Willingness.to.use.Mobile.Banking", data=fisheries)
(res <- wilcox.test(Education ~ factor(Willingness.to.use.Mobile.Banking), alternative="two.sided", data=fisheries))
group.names <- c(group.names, "Willingness.to.use.Mobile.Banking=0")
group.min <- c(group.min, with(fisheries, min(Education[Willingness.to.use.Mobile.Banking=='0'], na.rm=TRUE)))
group.1Q <- c(group.1Q, with(fisheries, quantile(Education[Willingness.to.use.Mobile.Banking=='0'], 0.25, na.rm=TRUE)))
group.median <- c(group.median, with(fisheries, median(Education[Willingness.to.use.Mobile.Banking=='0'], na.rm=TRUE)))
group.3Q <- c(group.3Q, with(fisheries, quantile(Education[Willingness.to.use.Mobile.Banking=='0'], 0.75, na.rm=TRUE)))
group.max <- c(group.max, with(fisheries, max(Education[Willingness.to.use.Mobile.Banking=='0'], na.rm=TRUE)))
group.p <- c(group.p, signif(res$p.value,digits=3))
group.names <- c(group.names, "Willingness.to.use.Mobile.Banking=1")
group.min <- c(group.min, with(fisheries, min(Education[Willingness.to.use.Mobile.Banking=='1'], na.rm=TRUE)))
group.1Q <- c(group.1Q, with(fisheries, quantile(Education[Willingness.to.use.Mobile.Banking=='1'], 0.25, na.rm=TRUE)))
group.median <- c(group.median, with(fisheries, median(Education[Willingness.to.use.Mobile.Banking=='1'], na.rm=TRUE)))
group.3Q <- c(group.3Q, with(fisheries, quantile(Education[Willingness.to.use.Mobile.Banking=='1'], 0.75, na.rm=TRUE)))
group.max <- c(group.max, with(fisheries, max(Education[Willingness.to.use.Mobile.Banking=='1'], na.rm=TRUE)))
group.p <- c(group.p, "")
mannwhitney.table <- NULL
mannwhitney.table <- data.frame(Minimum=group.min, Q1=group.1Q, Median=group.median, Q3=group.3Q, Maximum=group.max, p.value=group.p)
rownames(mannwhitney.table) <- group.names
colnames(mannwhitney.table)[c(2,4)] <- c("25%", "75%")
colnames(mannwhitney.table) <- gettextRcmdr(colnames(mannwhitney.table))
mannwhitney.table
#####Numerical summaries#####
res <- NULL
res <- numSummary(fisheries[,"Average.Per.day.sales"], groups=fisheries$Customer.request.for.digital.payment, statistics=c("mean", "sd", "quantiles"), 
  quantiles=c(0,.25,.5,.75,1))
colnames(res$table)[1:2] <- gettextRcmdr( colnames(res$table)[1:2])
res
#####Mann-Whitney U test#####
group.names <- NULL
group.median <- NULL
group.min <- NULL
group.max <- NULL
group.1Q <- NULL
group.3Q <- NULL
group.p <- NULL
windows(width=7, height=7); par(lwd=1, las=1, family="sans", cex=1, mgp=c(3.0,1,0))
boxplot(Average.Per.day.sales~ factor(Customer.request.for.digital.payment), ylab="Average.Per.day.sales", xlab="Customer.request.for.digital.payment", 
  data=fisheries)
(res <- wilcox.test(Average.Per.day.sales ~ factor(Customer.request.for.digital.payment), alternative="two.sided", data=fisheries))
group.names <- c(group.names, "Customer.request.for.digital.payment=0")
group.min <- c(group.min, with(fisheries, min(Average.Per.day.sales[Customer.request.for.digital.payment=='0'], na.rm=TRUE)))
group.1Q <- c(group.1Q, with(fisheries, quantile(Average.Per.day.sales[Customer.request.for.digital.payment=='0'], 0.25, na.rm=TRUE)))
group.median <- c(group.median, with(fisheries, median(Average.Per.day.sales[Customer.request.for.digital.payment=='0'], na.rm=TRUE)))
group.3Q <- c(group.3Q, with(fisheries, quantile(Average.Per.day.sales[Customer.request.for.digital.payment=='0'], 0.75, na.rm=TRUE)))
group.max <- c(group.max, with(fisheries, max(Average.Per.day.sales[Customer.request.for.digital.payment=='0'], na.rm=TRUE)))
group.p <- c(group.p, signif(res$p.value,digits=3))
group.names <- c(group.names, "Customer.request.for.digital.payment=1")
group.min <- c(group.min, with(fisheries, min(Average.Per.day.sales[Customer.request.for.digital.payment=='1'], na.rm=TRUE)))
group.1Q <- c(group.1Q, with(fisheries, quantile(Average.Per.day.sales[Customer.request.for.digital.payment=='1'], 0.25, na.rm=TRUE)))
group.median <- c(group.median, with(fisheries, median(Average.Per.day.sales[Customer.request.for.digital.payment=='1'], na.rm=TRUE)))
group.3Q <- c(group.3Q, with(fisheries, quantile(Average.Per.day.sales[Customer.request.for.digital.payment=='1'], 0.75, na.rm=TRUE)))
group.max <- c(group.max, with(fisheries, max(Average.Per.day.sales[Customer.request.for.digital.payment=='1'], na.rm=TRUE)))
group.p <- c(group.p, "")
mannwhitney.table <- NULL
mannwhitney.table <- data.frame(Minimum=group.min, Q1=group.1Q, Median=group.median, Q3=group.3Q, Maximum=group.max, p.value=group.p)
rownames(mannwhitney.table) <- group.names
colnames(mannwhitney.table)[c(2,4)] <- c("25%", "75%")
colnames(mannwhitney.table) <- gettextRcmdr(colnames(mannwhitney.table))
mannwhitney.table
library(abind, pos=16)
#####Create two-way table and compare two proportions (Fisher's exact test)#####
Fisher.summary.table <- NULL
.Table <- NULL
.Table <- xtabs(~Bank.Name+Debit.Card, data=fisheries)
.Table
.Test <- chisq.test(.Table, correct=FALSE)
.Test
.Test$expected # Expected Counts
remove(.Test)
res <- NULL
res <- chisq.test(.Table, correct=FALSE)
Fisher.summary.table <- rbind(Fisher.summary.table, summary.table.twoway(table=.Table, res=res))
colnames(Fisher.summary.table)[length(Fisher.summary.table)] <-  gettextRcmdr( colnames(Fisher.summary.table)[length(Fisher.summary.table)])
Fisher.summary.table
#####Create two-way table and compare two proportions (Fisher's exact test)#####
Fisher.summary.table <- NULL
.Table <- NULL
.Table <- xtabs(~Bank.Name+Debit.Card, data=fisheries)
.Table
fisher.test(.Table)
res <- NULL
res <- fisher.test(.Table)
Fisher.summary.table <- rbind(Fisher.summary.table, summary.table.twoway(table=.Table, res=res))
colnames(Fisher.summary.table)[length(Fisher.summary.table)] <-  gettextRcmdr( colnames(Fisher.summary.table)[length(Fisher.summary.table)])
Fisher.summary.table

